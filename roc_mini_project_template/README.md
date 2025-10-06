# Mini Project 1 — Regeneration Organizing Cell (ROC) in *Xenopus* Tail

This repository contains a Colab‑ready pipeline to identify the **Regeneration Organizing Cell (ROC)** in the frog tail single‑cell RNA‑seq data, reproduce clustering, select ROC markers, compare with **Supplementary Table 3**, and evaluate denoising + batch integration effects.

## Quickstart (Google Colab)
1. Open `notebooks/roc_pipeline.ipynb` in Google Colab.
2. Run the first cell to install Python packages.
3. Provide the data path or URL when prompted (download the data from the journal website or the course link).
4. Run all cells to reproduce the figures and outputs under `results/`.

## Repository Layout
```
roc_mini_project_template/
├── notebooks/
│   └── roc_pipeline.ipynb
├── src/
│   └── utils.py
├── data/
│   └── README.md
├── results/
│   ├── README.md
│   └── figs/
├── report_template/
│   └── report_template.md
├── requirements.txt
├── environment.yml
├── LICENSE
├── .gitignore
└── README.md
```

## Code Availability
All code is under MIT License. Include your public GitHub link in the report.

## MI‑Checklist
Please complete the MI‑Checklist and include a link in your write‑up:
- https://www.nature.com/articles/s41591-020-1041-y/tables/1
