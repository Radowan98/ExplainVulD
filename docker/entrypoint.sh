#!/bin/sh
set -e

echo "--- Setting up the demo environment ---"

echo "[1/2] Creating directory cpgs/chrome..."
mkdir -p cpgs/chrome

echo "[2/2] Unzipping chrome CPGs into cpgs/chrome..."
unzip -q cpg_dot_files/chrome_cpgs.zip -d cpgs/chrome
echo "--- Setup complete ---"
echo ""

echo "--- Running the dataset cleaning demo (scripts/clean_dataset.py) ---"
python scripts/clean_dataset.py
echo ""
echo "--- Demo finished ---"
echo "Cleaned graphs are available in the container at /app/cpgs/c_chrome"
