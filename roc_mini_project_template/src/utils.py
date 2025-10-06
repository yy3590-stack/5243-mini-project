import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score, silhouette_score
from typing import List, Dict

def compute_ari(labels_true, labels_pred):
    return adjusted_rand_score(labels_true, labels_pred)

def compute_silhouette(X_embedded, cluster_labels, metric='euclidean'):
    return silhouette_score(X_embedded, cluster_labels, metric=metric)

def purity_score(y_true, y_pred):
    contingency_matrix = pd.crosstab(pd.Series(y_true, name='true'), pd.Series(y_pred, name='pred'))
    return np.sum(np.max(contingency_matrix.values, axis=0)) / np.sum(contingency_matrix.values)

def overlap_stats(query: List[str], reference: List[str]) -> Dict[str, float]:
    q = set([g.strip().upper() for g in query if isinstance(g, str)])
    r = set([g.strip().upper() for g in reference if isinstance(g, str)])
    inter = q & r
    jaccard = len(inter) / max(1, len(q | r))
    precision = len(inter) / max(1, len(q))
    recall = len(inter) / max(1, len(r))
    return {'jaccard': jaccard, 'precision': precision, 'recall': recall, 'overlap_n': len(inter)}

def save_markers(adata, key='rank_genes_groups', out_csv='results/markers_top.csv', n_top=20):
    import scanpy as sc
    if key not in adata.uns:
        raise ValueError(f'{key} not found in adata.uns')
    df = sc.get.rank_genes_groups_df(adata, group=None)
    df = df.groupby('group').head(n_top)
    df.to_csv(out_csv, index=False)
    return df

def ensure_categorical(obs, key):
    if obs[key].dtype.name != 'category':
        obs[key] = obs[key].astype('category')
    return obs[key]
