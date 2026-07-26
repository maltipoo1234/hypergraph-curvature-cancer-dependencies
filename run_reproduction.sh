#!/bin/bash
set -e
cd "$(dirname "$0")"

PYTHON_EXE=python3
PIP_EXE="python3 -m pip"

echo "[1/5] Checking environment and dependencies..."
if [ -f "requirements.txt" ]; then
    $PIP_EXE install -r requirements.txt --quiet
fi

echo "[2/5] Running Core Unit Tests..."
$PYTHON_EXE -u curvature_lib.py

echo "[3/5] Executing Main Analysis Pipeline..."
# This handles: Data Audit, Topology Build, Discovery, Cross-Topology Audit,
# Tight Null Framework (Adaptive Permutations), and Clinical/Pharmacologic Bridges.
$PYTHON_EXE -u curvature_pipeline.py

echo "[4/5] Executing External Validation (Sanger, DepMap 25Q3)..."
# This calculates Frequentist Meta-Analysis and Bayesian MCMC convergence (R-hat).
$PYTHON_EXE -u curvature_validation.py

echo "[5/5] Running Robustness & Sensitivity Analysis..."
# This sweeps through thresholds to prove results are not dependent on magic numbers.
$PYTHON_EXE -u curvature_robustness.py

echo "it ended"
