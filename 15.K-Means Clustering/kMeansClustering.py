# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 00:43:03 2018

@author: Arnob
"""

# import lib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import dataset
dataset = pd.read_csv('Mall_Customers.csv')

# here we take anual income and spending (label)
X = dataset.iloc[:, [3,4]].values

# using the Elbow method to find the optimal number of cluster 
# import kmeans lib
from sklearn.cluster import KMeans

# within cluster sum of square(WCSS)
wcss = []  

# Calculate 10 defferent number of wcss 
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, 
                    init = 'k-means++', 
                    max_iter = 300, 
                    n_init = 10, 
                    random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Cluster')
plt.xlabel('wcss')
plt.show()    

# Applying k-measn to the mall dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 32)
y_kmeans = kmeans.fit_predict(X)    

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], 
            kmeans.cluster_centers_[:, 1], 
            s = 300, c = 'yellow', 
            label = 'Centroids')

plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


