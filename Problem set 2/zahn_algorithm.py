import EMST as EMST
import networkx as nx

k = 2

X = [[1, 10], [200, 4], [3, 7], [5,70], [4,4], [310, 900], [0,0], [40,100], [210,1000]]

def zahn_algorithm(X, k):
	print "* Points:\n", X, "\n"

	Graph = nx.complete_graph(len(X), create_using=None)

	for u,v,d in Graph.edges(data=True):
			d['weight']=EMST.distance(X[u],X[v])

	T = nx.minimum_spanning_tree(Graph)

	print"* EMST of the data: \n", sorted(T.edges(data=False), reverse=True), "\n"


	print "*", k, " Clusters: "
	for i in range(0, k-1):
		edge = max(T.edges(data=True))
		T.remove_edge(edge[0],edge[1])
		CCs = sorted(nx.connected_components(T), key = len, reverse=True)
		print(CCs)


