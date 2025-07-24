# ExplainVulD Dataset Release

This repository contains the dataset and Code Property Graph (CPG) files used in the study:

**"Explainable Vulnerability Detection in C/C++ Using Edge-Aware Graph Attention Networks"**  
by Radowanul Haque, Aftab Ali, Sally McClean, and Naveed Khan (2025)  
[arXiv:2507.16540](https://arxiv.org/abs/2507.16540)

---

## 📦 Contents

This release includes:

- `data/functions_chrome.jsonl` — Function-level vulnerability data from Google Chrome.
- `data/functions_debian.jsonl` — Function-level vulnerability data from Debian.
- `cpg_dot_files/chrome_cpgs.zip` — CPG DOT files for Chrome functions.
- `cpg_dot_files/debian_cpgs.zip` — CPG DOT files for Debian functions.
- `scripts/clean_dataset.py` — Removes malformed graphs (e.g., missing CFG or >500 nodes).
- `scripts/dot_to_pdf.py` — Converts individual DOT files into visual PDFs.
- `docs/dataset_description.md` — Detailed format and field explanation.

> 🛠️ No training or evaluation code is included. This repository focuses solely on the experimental data used in the ExplainVulD study.

---

## 🔍 Visualising CPG Graphs

To convert a DOT file to PDF:

```bash
python scripts/dot_to_pdf.py --input path/to/graph.dot --output path/to/graph.pdf
