import networkx as nx

def BFS(graph):
	cc = sorted(nx.connected_components(graph), key = len, reverse=True)
	return cc


