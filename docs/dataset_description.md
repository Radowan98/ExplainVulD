# Dataset Description

This document provides an overview of the dataset released in the ExplainVulD study. It describes the data structure, preprocessing criteria, and statistics before and after cleaning.

## 1. Overview

The dataset is a curated subset of the ReVeal vulnerability detection dataset. It includes function-level source code samples extracted from two large open-source C/C++ projects: **Google Chrome** and **Debian**.

Each function is labeled as either:
- `1` — Vulnerable
- `0` — Safe

Each function also has a corresponding **Code Property Graph (CPG)** in DOT format that represents AST, CFG, and DFG edges.

## 2. File Naming Convention

Each function is saved in a `.c` file with the following naming scheme:

```
<project>_<id>_<label>.c
```

- `<project>`: either `chrome` or `debian`
- `<id>`: integer ID of the function
- `<label>`: `0` (safe) or `1` (vulnerable)

Examples:
- `chrome_1_0.c` → Chrome function ID 1, safe
- `debian_42_1.c` → Debian function ID 42, vulnerable

Corresponding CPG files follow the same name but with `.dot` extension.

## 3. Cleaning Criteria

Functions were filtered based on the following conditions:
- CPG must contain at least one **CFG edge**
- Total number of nodes in the CPG must not exceed **500**

Any DOT files that failed to meet these conditions were excluded. Removed file names are logged in `removed_files_log.json`.

## 4. Dataset Statistics

### Table 1: Distribution *before* data cleaning

| Project | Vulnerable | Safe   | Vulnerable (%) |
|---------|------------|--------|----------------|
| Chrome  | 825        | 3,611  | 22.85          |
| Debian  | 1,415      | 16,883 | 8.38           |
| **Total** | **2,240** | **20,494** | **10.93**    |

### Table 2: Distribution *after* data cleaning

| Project | Vulnerable | Safe   | Vulnerable (%) |
|---------|------------|--------|----------------|
| Chrome  | 577        | 2,377  | 19.53          |
| Debian  | 896        | 13,861 | 6.06           |
| **Total** | **1,473** | **16,238** | **8.32**    |

## 5. Citation Guidelines

If you use the **original dataset** content, please cite ReVeal:

> Chakraborty et al., "Deep Learning based Vulnerability Detection: Are We There Yet?", arXiv:2009.07235.  
> [https://arxiv.org/abs/2009.07235](https://arxiv.org/abs/2009.07235)

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
