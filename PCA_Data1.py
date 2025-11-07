import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = np.array([
    [1, 2, 3, 4],
    [5, 5, 6, 7],
    [1, 4, 2, 3],
    [5, 3, 2, 1],
    [8, 1, 2, 2]
], dtype=float)

df = pd.DataFrame(data, columns=['f1', 'f2', 'f3', 'f4'])
print("Original Data:\n", df, "\n")

means = df.mean(axis=0)
centered = df - means
print("Mean of each feature:\n", means, "\n")
print("Centered Data (mean = 0):\n", centered, "\n")

cov_matrix = np.cov(centered, rowvar=False)
print("Covariance Matrix:\n", pd.DataFrame(cov_matrix, index=df.columns, columns=df.columns), "\n")

eigvals, eigvecs = np.linalg.eigh(cov_matrix)

idx = np.argsort(eigvals)[::-1]
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

print("Eigenvalues (descending):\n", eigvals, "\n")
print("Eigenvectors (columns are PCs):\n",
pd.DataFrame(eigvecs, index=df.columns, columns=['PC1', 'PC2', 'PC3', 'PC4']), "\n")

explained_variance_ratio = eigvals / eigvals.sum()
print("Explained Variance Ratio:\n", explained_variance_ratio, "\n")

projected = centered.dot(eigvecs)
proj_df = pd.DataFrame(projected, columns=['PC1', 'PC2', 'PC3', 'PC4'])
print("Projected Data (Principal Component Scores):\n", proj_df, "\n")

pca = PCA(n_components=4)
pca.fit(df)
print("sklearn PCA - Explained Variance Ratio:\n", pca.explained_variance_ratio_)
print("sklearn PCA - Components (PC directions):\n",
      pd.DataFrame(pca.components_, columns=df.columns, index=['PC1', 'PC2', 'PC3', 'PC4']), "\n")

# Step 9: Visualization (first two PCs)
plt.figure(figsize=(6, 5))
plt.scatter(proj_df['PC1'], proj_df['PC2'], color='blue', s=100)
for i, txt in enumerate(df.index):
    plt.annotate(f"Sample {i+1}", (proj_df['PC1'][i]+0.1, proj_df['PC2'][i]))
plt.title("PCA Projection (PC1 vs PC2)")
plt.xlabel(f"PC1 ({explained_variance_ratio[0]*100:.2f}% variance)")
plt.ylabel(f"PC2 ({explained_variance_ratio[1]*100:.2f}% variance)")
plt.grid(True)
plt.show()
