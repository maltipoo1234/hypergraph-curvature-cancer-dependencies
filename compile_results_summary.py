#!/usr/bin/env python3
"""
compile_results_summary.py
Automated high-fidelity numerical consolidation and summary generator.
Gathers data across all parquet tables and robustness summaries into one markdown report.
"""

import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime

pd.set_option('future.no_silent_downcasting', True)

def format_df_for_md(df, max_str_len=60):
    """Safely format dataframe columns for markdown display with rounding and truncation."""
    df_cooked = df.copy()
    for col in df_cooked.columns:
        if pd.api.types.is_float_dtype(df_cooked[col]):
            df_cooked[col] = df_cooked[col].round(6)
        else:
            df_cooked[col] = df_cooked[col].astype(str).apply(
                lambda x: "" if x in ["nan", "None", "<NA>"] else (x if len(x) <= max_str_len else x[:max_str_len-3] + "...")
            )
    return df_cooked

def main():
    root = Path(__file__).resolve().parent
    tables_dir = root / "results/tables"
    robustness_dir = root / "results/robustness"
    output_dir = root / "results/reports"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    output_md_path = output_dir / "comprehensive_numerical_summary.md"
    
    print(f"[*] Starting compilation of pipeline results...")
    print(f"[*] Looking for tables in: {tables_dir}")
    print(f"[*] Looking for robustness metrics in: {robustness_dir}")
    
    # Gather files
    files_to_process = []
    
    if tables_dir.exists():
        for f in tables_dir.glob("*.parquet"):
            files_to_process.append((f, "Parquet Table"))
    
    if robustness_dir.exists():
        for f in robustness_dir.glob("*.csv"):
            files_to_process.append((f, "Robustness CSV"))
        for f in robustness_dir.glob("*.parquet"):
            files_to_process.append((f, "Robustness Parquet"))
            
    # Sort files alphabetically to ensure structured ordering
    files_to_process.sort(key=lambda x: x[0].name)
    
    if not files_to_process:
        print("[-] Error: No result data files found. Please ensure the pipeline has run successfully.")
        sys.exit(1)
        
    print(f"[+] Found {len(files_to_process)} data files to summarize.")
    
    with open(output_md_path, "w", encoding="utf-8") as md:
        # Document Header
        md.write("# Hypergraph Curvature Pipeline: Comprehensive Numerical Summary\n\n")
        md.write(f"- **Generated On:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        md.write(f"- **Total Input Files Processed:** {len(files_to_process)}\n")
        md.write("- **Target Purpose:** Direct manuscript results writing and statistical verification.\n\n")
        
        md.write("## Table of Contents\n")
        for idx, (f_path, f_type) in enumerate(files_to_process, 1):
            md.write(f"{idx}. [{f_path.name}](#file-{f_path.name.lower().replace('.', '-')})\n")
        md.write("\n---\n\n")
        
        # Process each file
        for idx, (f_path, f_type) in enumerate(files_to_process, 1):
            print(f"    -> Processing [{idx}/{len(files_to_process)}]: {f_path.name}")
            
            md.write(f"## File: {f_path.name}\n\n")
            md.write(f"- **Source Framework Category:** {f_type}\n")
            md.write(f"- **Project Relative Path:** `{f_path.relative_to(root)}`\n")
            
            try:
                # Read data depending on extension
                if f_path.suffix == ".parquet":
                    df = pd.read_parquet(f_path)
                elif f_path.suffix == ".csv":
                    df = pd.read_csv(f_path)
                else:
                    continue
                
                rows, cols = df.shape
                md.write(f"- **Matrix Dimensions:** {rows} rows × {cols} columns\n\n")
                
                # 1. Schema & Data Quality Audit
                md.write("### 1. Data Schema & Quality Audit\n\n")
                schema_records = []
                for col in df.columns:
                    non_null = df[col].notnull().sum()
                    null_cnt = rows - non_null
                    null_pct = (null_cnt / rows) * 100 if rows > 0 else 0
                    schema_records.append({
                        "Column Name": col,
                        "Dtype": str(df[col].dtype),
                        "Non-Null Count": non_null,
                        "Null Count": null_cnt,
                        "Null %": f"{null_pct:.2f}%"
                    })
                schema_df = pd.DataFrame(schema_records)
                md.write(schema_df.to_markdown(index=False) + "\n\n")
                
                # 2. Descriptive Statistics (Transposed for easy vertical scrolling)
                md.write("### 2. Full Descriptive Summary Statistics\n\n")
                desc_df = df.describe(include='all').T
                desc_df = desc_df.fillna("—")
                # Clean floats inside the description table
                for col in desc_df.columns:
                    desc_df[col] = desc_df[col].apply(lambda x: f"{x:.6f}" if isinstance(x, (float, np.floating)) else str(x))
                md.write(desc_df.to_markdown(index=True) + "\n\n")
                
                # 3. Value Distributions for Grouping/Categorical Columns
                categorical_cols = [c for c in df.columns if df[c].dtype == 'object' or str(df[c].dtype) in ['category', 'bool', 'boolean']]
                valid_cats = [c for c in categorical_cols if 1 < df[c].nunique() <= 15]
                
                if valid_cats:
                    md.write("### 3. Categorical Distribution Breakdown\n\n")
                    for cat in valid_cats:
                        v_counts = df[cat].value_counts(dropna=False)
                        v_pcts = df[cat].value_counts(dropna=False, normalize=True) * 100
                        dist_df = pd.DataFrame({
                            "Value Category": v_counts.index,
                            "Absolute Count": v_counts.values,
                            "Percentage Proportion": v_pcts.values
                        })
                        dist_df["Percentage Proportion"] = dist_df["Percentage Proportion"].round(2).astype(str) + "%"
                        md.write(f"**Column Grouping: `{cat}`**\n\n")
                        md.write(dist_df.to_markdown(index=False) + "\n\n")
                
                # 4. Automated Statistical Highlights Discovery
                md.write("### 4. Significant Signals & Key Highlights\n\n")
                highlight_triggered = False
                
                # Dynamic detection of P-values / Significance bounds
                p_cols = [c for c in df.columns if any(k in c.lower() for k in ["p_value", "pvalue", "q_value", "qvalue", "fdr", "meta_p", "bayes_p"])]
                for p_col in p_cols:
                    if pd.api.types.is_numeric_dtype(df[p_col]):
                        sig_mask = df[p_col] < 0.05
                        sig_count = sig_mask.sum()
                        if sig_count > 0:
                            md.write(f"- 💡 **Significance Hit:** Column `{p_col}` contains **{sig_count}** records with a nominal significance value ($P < 0.05$).\n")
                            # Show the top 5 most significant rows
                            top_sig = df.nsmallest(min(5, sig_count), p_col)
                            md.write("\n*Top localized significance indices:*\n\n")
                            md.write(format_df_for_md(top_sig).to_markdown(index=False) + "\n\n")
                            highlight_triggered = True
                
                # Concordance indices
                con_cols = [c for c in df.columns if "concordance" in c.lower() or "rate" in c.lower()]
                for c_col in con_cols:
                    if pd.api.types.is_numeric_dtype(df[c_col]):
                        md.write(f"- 📊 **Concordance Metric Profile (`{c_col}`):** Mean={df[c_col].mean():.5f}, Max={df[c_col].max():.5f}, Min={df[c_col].min():.5f}\n")
                        highlight_triggered = True
                        
                # Correlation check
                corr_cols = [c for c in df.columns if any(k in c.lower() for k in ["rho", "pearson_r", "spearman", "roc_auc", "average_precision"])]
                for corr_col in corr_cols:
                    if pd.api.types.is_numeric_dtype(df[corr_col]):
                        top_idx = df[corr_col].idxmax()
                        max_val = df[corr_col].max()
                        md.write(f"- 📈 **Peak Performance Asset (`{corr_col}`):** Maximal value observed is `{max_val:.5f}`.\n")
                        highlight_triggered = True
                
                if not highlight_triggered:
                    md.write("*No default statistical signature triggers detected in this matrix header structure.*\n\n")
                else:
                    md.write("\n")
                
                # 5. High-Fidelity Data Matrix Dump (Complete or Extended Head/Tail)
                md.write("### 5. High-Fidelity Data Preview\n\n")
                if rows <= 120:
                    md.write(f"Showing entire dataset content row footprint ({rows} rows total):\n\n")
                    md.write(format_df_for_md(df).to_markdown(index=False) + "\n\n")
                else:
                    md.write(f"Dataset exceeds threshold size limit for full text inline display. Rendering stratified margins (Top 40 & Bottom 40 boundaries):\n\n")
                    md.write("**First 40 Structural Rows:**\n\n")
                    md.write(format_df_for_md(df.head(40)).to_markdown(index=False) + "\n\n")
                    md.write(f"\n*... [Truncated {rows - 80} standard row items inline] ...*\n\n")
                    md.write("**Last 40 Structural Rows:**\n\n")
                    md.write(format_df_for_md(df.tail(40)).to_markdown(index=False) + "\n\n")
                
                md.write("\n---\n\n")
                
            except Exception as e:
                md.write(f"❌ **Compilation Error:** Failed to parse or handle file content matrix pipeline step: `{str(e)}`\n\n---\n\n")
                print(f"    [!] Error parsing {f_path.name}: {str(e)}")

    print(f"[+] Complete process finished. Comprehensive document exported to: {output_md_path}")

if __name__ == "__main__":
    main()