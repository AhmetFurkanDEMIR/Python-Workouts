from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 3]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
print(kmeans.labels_)

print(kmeans.predict([[0, 0], [12, 3]]))

print(kmeans.cluster_centers_)