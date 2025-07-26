# ExplainVulD Dataset Release

This repository contains the dataset and Code Property Graph (CPG) files used in the study:

**"Explainable Vulnerability Detection in C/C++ Using Edge-Aware Graph Attention Networks"**  
by Radowanul Haque, Aftab Ali, Sally McClean, and Naveed Khan (2025)  
📄 [arXiv:2507.16540](https://arxiv.org/abs/2507.16540)

---

## 📦 Repository Contents

```
ExplainVulD-Dataset/
├── data/
│   ├── chrome.zip                     # Vulnerability-labelled Chrome functions
│   └── debian.zip                     # Vulnerability-labelled Debian functions
│
├── cpg_dot_files/
│   ├── chrome_cpgs.zip                # DOT-format CPGs for Chrome functions
│   └── debian_cpgs.zip                # DOT-format CPGs for Debian functions
│
├── scripts/
│   ├── clean_dataset.py               # Removes DOTs with no CFG or >500 nodes
│   └── dot_to_pdf.py                  # Converts DOT files to PDF
│
├── docs/
│   └── dataset_description.md         # Field-level details and usage guide
│
├── README.md                          # This file
└── LICENSE                            
```

---

## 📊 Dataset Summary

Each function is labelled using the filename format:  
`<project>_<id>_<label>.c`

For example:
- `chrome_1_0.c` → Chrome function, ID 1, label `0` (safe)  
- `debian_2_1.c` → Debian function, ID 2, label `1` (vulnerable)

Corresponding CPGs use the same naming convention as `.dot` files.

This dataset is derived from the original **ReVeal** dataset:

> **Chakraborty et al.**, *"Deep Learning based Vulnerability Detection: Are We There Yet?"*,  
> arXiv:2009.07235 — [https://arxiv.org/abs/2009.07235](https://arxiv.org/abs/2009.07235)

We have curated and filtered ReVeal to extract functions from Chrome and Debian, generated corresponding Code Property Graphs (CPGs), and removed malformed or oversized graphs to support explainable GNN-based vulnerability detection.

---

## 🔧 Usage

### 1. Visualise a CPG DOT File

To convert a `.dot` file into a PDF:

```bash
python scripts/dot_to_pdf.py --input path/to/graph.dot --output path/to/graph.pdf
```

Ensure Graphviz is installed:

```bash
# Ubuntu
sudo apt-get install graphviz

# macOS
brew install graphviz
```

### 2. Clean Raw DOT Files

To remove graphs that are malformed (missing CFG) or too large (>500 nodes):

```bash
python scripts/clean_dataset.py --input_dir path/to/dot_files --output_dir path/to/cleaned
```

Use this after unzipping `chrome_cpgs.zip` or `debian_cpgs.zip`.

---

## 📚 Citation
If you use the **processed Code Property Graphs (CPGs)** or the dataset split and filtering provided in this repository, please cite our ExplainVulD study:

```bibtex
@misc{haque2025explainablevulnerabilitydetectioncc,
  title        = {Explainable Vulnerability Detection in C/C++ Using Edge-Aware Graph Attention Networks},
  author       = {Radowanul Haque and Aftab Ali and Sally McClean and Naveed Khan},
  year         = {2025},
  eprint       = {2507.16540},
  archivePrefix= {arXiv},
  primaryClass = {cs.CR},
  url          = {https://arxiv.org/abs/2507.16540}
}



## 🐳 Docker Support

You can run ExplainVulD’s Code Property Graph (CPG) visualisation tool using Docker:

```bash
docker pull remyxai/2507.16540v1:latest
docker run -it remyxai/2507.16540v1

