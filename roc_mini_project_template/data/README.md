# Data Folder

Place the raw single‑cell RNA‑seq matrices and metadata here.
Typical formats: `h5ad`, `mtx` + `tsv`, `loom`, or `h5` (10x).

Recommended structure:
```
data/
├── counts.h5ad
├── meta.csv  # optional, if not embedded in AnnData
└── supp_table3_genes.txt  # paste the genes from Supplementary Table 3 (one per line)
```
