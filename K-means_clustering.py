import numpy as np

np.random.seed(42)

cluster_1 = np.random.randn(100, 2) + np.array([2, 2])
cluster_2 = np.random.randn(100, 2) + np.array([8, 8])
cluster_3 = np.random.randn(100, 2) + np.array([2, 8])

X = np.vstack((cluster_1, cluster_2, cluster_3))

k = 3

centroids = X[np.random.choice(len(X), k, replace=False)]

for _ in range(100):
    distances = np.sqrt(((X[:, np.newaxis] - centroids) ** 2).sum(axis=2))
    labels = np.argmin(distances, axis=1)

    new_centroids = np.array([
        X[labels == i].mean(axis=0)
        for i in range(k)
    ])

    if np.allclose(centroids, new_centroids):
        break

    centroids = new_centroids

print("Final Centroids:")
print(centroids)

print("\nCluster Distribution:")
for i in range(k):
    print(f"Cluster {i}: {np.sum(labels == i)} points")