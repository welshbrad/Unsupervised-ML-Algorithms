# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from copy import copy, deepcopy
from numpy import linalg as LA
import math as m
from sklearn.neighbors import kneighbors_graph
from sklearn import manifold, datasets

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.decomposition import IncrementalPCA

"""
Implement MDS 

"""
def my_MDS(dists, k):
	
	#construct P^2 from P
	P2 = deepcopy(dists)
	for i in range(len(P2)):
		for j in range(len(P2[i])):
			P2[i][j] = dists[i][j]**2;
	
	#construct N*N identity matrix
	I = deepcopy(dists)
	for i in range(len(I)):
		for j in range(len(I[i])):
			if i == j:
				I[i][j] = 1
			else:
				I[i][j] = 0
	J = deepcopy(I) #set J mat to Identity Matrix of NxN
	for i in range(len(J)):
		for j in range(len(J[i])):
			J[i][j] = (I[i][j]-.25)
	B = deepcopy(J)
	for i in range(len(B)):
		for j in range(len(B[i])):
			B[i][j] = -0.5*B[i][j]	
	result = np.matmul(B, P2)
	B = np.matmul(result, J)
	
	eigVals, eigVecs = LA.eig(B)
	i = eigVals.argsort()[-k:][::-1]
	eigVals = eigVals[i]
	eigVecs = eigVecs[:,i]
	
	X = [[0 for x in range(k)] for y in range(k)] 
	for i in range(k):
		for j in range(k):
			if i==j:
				X[i][j] = m.sqrt(eigVals[i])
			else:
				X[i][j] = 0

	
	return (np.matmul(eigVecs, X))

'''
dists = [[0, 93, 82, 133],
		 [93, 0, 52, 60],
		 [82, 52, 0, 111],
		 [133, 60, 111, 0]]

MDS(dists, 2)
'''


def ISOMAP(X, n_components, n_neighbors):

	neighborhood_graph_matrix = kneighbors_graph(X, n_neighbors, mode='distance', include_self=False, n_jobs=-1).toarray()
	neighborhood_graph_graph = nx.from_numpy_matrix(neighborhood_graph_matrix)
	min_distances_list = nx.floyd_warshall_numpy(neighborhood_graph_graph).tolist()
	#my version
	coords = my_MDS(min_distances_list, n_components)
	
	#sklearn version
	#mds = manifold.MDS(n_components, dissimilarity='precomputed', max_iter=100, n_init=1)
	#coords = mds.fit_transform(min_distances_list)
	
	return coords
	



n_points = 100
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_components = 2
n_neighbors = 10

#ISOMAP Test
POINTS = ISOMAP(X, n_components, n_neighbors)
#

#MDS Test

#X = euclidean_distances(X,X)
#POINTS = my_MDS(X, n_components)
#


#PCA Test

#ipca = IncrementalPCA(n_components=n_components, batch_size=3)
#ipca.fit(X)
#IncrementalPCA(batch_size=3, copy=True, n_components=n_components, whiten=False)
#ipca.transform(X) 
#POINTS = X
#


fig = plt.figure(figsize=(15, 8))
plt.suptitle("Manifold Learning with %i points, %i neighbors"
             % (n_points, n_neighbors), fontsize=14)

ax = fig.add_subplot(251, projection='3d')
ax.scatter(POINTS[:, 0], POINTS[:, 1], c=color, cmap=plt.cm.Spectral)
plt.show()
