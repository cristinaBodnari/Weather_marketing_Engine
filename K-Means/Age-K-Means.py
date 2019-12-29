import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist

#Load input data
X = pd.read_csv('Age_K_Means.txt')



# Determine k by minimizing the distortion -
# the sum of the squared distances between each observation vector and its centroid
distortions = []
K = range(1,10)
for k in K:
   k_model = KMeans(n_clusters=k).fit(X)
   k_model.fit(X)
   dist = sum(np.min(cdist(X, k_model.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0]
   distortions.append(dist)
print(distortions)

plt.title('Elbow Method for Optimal K')
plt.plot(K, distortions, 'bx-')
plt.xlabel('K')
plt.ylabel('Distortion')
plt.show()

# Optimal number of clusters K
num_clusters = 5

# Create K-Means classifier
kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=20)
# init: method of experimemtal finding the initial location of the centroids
# n_init: the algorithm will run n_init times with different cetroids and the best result of those will be taken

# Train the model
kmeans.fit(X)

y = kmeans.predict(X)
print(y)

