# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sklearn.manifold as skln

def draw_graph(G,pos): # this function is provided for you and you do not need to alter it.
     
     nx.draw_networkx_nodes(G, pos,
                       node_color='r',
                       node_size=500,
                       alpha=1)
     nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

#example of utilization of the above function

#(1) Define the graph G

G = nx.cubical_graph()

#(2) check the nodes of the graph G

print("the nodes of the graph are : ")
print(G.nodes())

#(3) define the position dictionary
pos = {0: np.array([ 0.82877618,  0.53211873]), 
       1: np.array([ 0.8059564,  0.       ]), 
       2: np.array([ 0.51148475,  0.37349706]), 
       3: np.array([ 0.54462887,  0.89200482]), 
       4: np.array([ 0.31695909,  0.62593525]), 
      5:np.array([ 0.02260257,  1.        ]), 
      6: np.array([ 0.        ,  0.46707769]), 
       7: np.array([ 0.28222528,  0.10714391])}

print("the position of the nodes of the graph are : ")
print(pos)


def graph_node_position_mds(G):
	for edge in G.edges():
   		G.add_edge(edge[0], edge[1], weight = 1)   
	A = nx.floyd_warshall_numpy(G)
	#print(G.edges(data=True))
	mds = skln.MDS(n_components=2, dissimilarity='precomputed')
	pos = mds.fit(A).embedding_
	return pos

def graph_node_position_Laplacian(G):
	for edge in G.edges():
	   		G.add_edge(edge[0], edge[1], weight = 1)   
	D = np.array(nx.floyd_warshall_numpy(G), ndmin=2)
	pos = skln.spectral_embedding(D, n_components=2)
	return pos


MDS_pos = graph_node_position_mds(G)
LAP_pos = graph_node_position_Laplacian(G)
draw_graph(G, MDS_pos)
plt.show()
draw_graph(G, LAP_pos)
plt.show()






