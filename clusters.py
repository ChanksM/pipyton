import numpy as np

from sklearn.cluster import KMeans

import pandas as pd

X = np.array([[185, 72],
              [170, 56],
              [168, 60],
              [179, 68],
              [182, 72],
              [188, 77]])

numpy_array = np.array(X)
df = pd.DataFrame(numpy_array, columns=['x', 'y'])

kmeans = KMeans(n_clusters=2)

kmeans.fit(X)x
df['c'] = kmeans.labels_
print('here')
print(df)

print(kmeans.cluster_centers_)

