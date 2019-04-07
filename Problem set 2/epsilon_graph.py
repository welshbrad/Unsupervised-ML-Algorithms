from sklearn.neighbors import radius_neighbors_graph
import networkx as nx
import numpy as np



def epsilon_graph(X, e):
	A = radius_neighbors_graph(X, e, mode='distance', include_self=False)
	A.toarray()
	return A
	
	
def epsilon_graph_clusters(X, e):
	A = epsilon_graph(X,e)
	Graph = nx.Graph(A)
	CC = sorted(nx.connected_components(Graph), key = len, reverse = True)
	return CC


