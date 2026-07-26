import os
import sys
import json
import pandas as pd
import numpy as np
from pathlib import Path
import subprocess
from curvature_lib import setup_logging

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "configs/pipeline_config.json"
RESULTS_DIR = ROOT / "results/robustness"

logger = setup_logging("curvature_robustness", ROOT / "logs")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def run_experiment(config_mod, label):
    logger.info(f"\n>>> Running Robustness Experiment: {label}")
    config = load_config()
    config.update(config_mod)
    
    # Save temporary config
    temp_config_path = ROOT / f"configs/temp_config_{label}.json"
    try:
        with open(temp_config_path, "w") as f:
            json.dump(config, f, indent=2)
            
        logger.info(f"  - Executing Pipeline with {temp_config_path}...")
        p_proc = subprocess.Popen([sys.executable, "-u", "curvature_pipeline.py", str(temp_config_path)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in p_proc.stdout:
            logger.info(f"    [Pipeline] {line.strip()}")
        p_proc.wait()
        
        logger.info(f"  - Executing Validation with {temp_config_path}...")
        v_proc = subprocess.Popen([sys.executable, "-u", "curvature_validation.py", str(temp_config_path)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in v_proc.stdout:
            logger.info(f"    [Validation] {line.strip()}")
        v_proc.wait()
        
        # Collect results
        sanger_sum = pd.read_parquet(ROOT / "results/tables/phase13_external_cmp_sanger_summary.parquet")
        depmap_sum = pd.read_parquet(ROOT / "results/tables/phase13_external_depmap25q3_summary.parquet")
        
        res = {
            "label": label,
            "sanger_concordance": sanger_sum["concordance_rate"].iloc[0],
            "sanger_p_neg": sanger_sum["bayes_p_negative"].iloc[0],
            "depmap_concordance": depmap_sum["concordance_rate"].iloc[0],
            "depmap_p_neg": depmap_sum["bayes_p_negative"].iloc[0],
        }
        res.update(config_mod)
        return res
    except Exception as e:
        logger.info(f"  - Experiment {label} FAILED: {e}")
        return None
    finally:
        if temp_config_path.exists():
            temp_config_path.unlink()

def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    experiments = [
        ({"mutation_min_mutant_models": 5}, "min_mut_5"),
        ({"mutation_min_mutant_models": 10}, "min_mut_10"),
        ({"corum_min_size": 2}, "corum_min_2"),
        ({"corum_min_size": 3}, "corum_min_3"),
    ]
    
    all_results = []
    summary_path = RESULTS_DIR / "robustness_summary.csv"
    base_seed = load_config().get("random_seed", 42)
    
    for i, (mod, label) in enumerate(experiments):
        # Inject modified seed to ensure unique statistical variance (avoids pseudo-replication)
        mod["random_seed"] = base_seed + i
        res = run_experiment(mod, label)
        if res:
            all_results.append(res)
            # Save incrementally
            pd.DataFrame(all_results).to_csv(summary_path, index=False)
            
    logger.info("\n--- ROBUSTNESS ANALYSIS COMPLETE ---")
    if all_results:
        logger.info(pd.DataFrame(all_results).to_string())
    logger.info(f"\nSummary saved to: {summary_path}")

if __name__ == "__main__":
    main()
