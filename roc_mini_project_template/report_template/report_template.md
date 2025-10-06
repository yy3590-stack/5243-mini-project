# Title: Identifying the Regeneration Organizing Cell (ROC) in *Xenopus* Tail

## Abstract (≤ 150 words)
Concise statement of data, methods, main result (cluster ID as ROC), top markers, and one‑line on denoising/integration impact.

## Introduction (≤ 0.5 page)
Biological background and problem statement. Cite the main paper. Clarify what ROC is and why it matters.

## Methods (≤ 1.5 pages)
**Data processing:** QC filters (genes/cell, counts, mito%), normalization, log1p, HVGs.  
**Dimensionality reduction:** PCA (n_comps), neighbors (k), UMAP/t‑SNE params.  
**Clustering:** at least two algorithms (e.g., Leiden, KMeans/GMM), with parameters.  
**Metrics:** ARI (if labels available), silhouette, purity.  
**Marker selection:** at least two methods (Wilcoxon & Logistic Regression).  
**Denoising:** at least two (e.g., MAGIC & MNN/DCA), how applied.  
**Batch integration over time:** at least two (e.g., BBKNN & Harmony), covariates used.  
**Code Availability:** link to your public GitHub and Colab.

## Results (≤ 1.5 pages)
**Figure 1 (Clustering):** UMAP colored by clusters/time; metric table.  
**Figure 2 (Gene analysis):** DotPlot/Heatmap of ROC markers; volcano plot.  
Identify ROC cluster + list top N markers; compare with Supplementary Table 3 (overlap, precision/recall).  
Summarize effects of denoising & integration on clusters and markers.

## Conclusion (≤ 0.5 page)
One paragraph: main discovery, robustness, caveats, and next steps.

## MI‑Checklist
Provide a filled checklist link.

## References
Main paper, methods packages, and any additional tools.
