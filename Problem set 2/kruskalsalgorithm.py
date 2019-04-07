#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unionfind import *
import networkx as nx


class kruskalsalgorithm():
    def __init__(self,inputgraph):
        self.original_graph=inputgraph
        self.tree=nx.Graph()
        
        self.sorted_edges=sorted(inputgraph.edges(data=True), key=lambda x: x[2]['weight'])


    def spanningtree(self):
    
	uf = UnionFind()
	#uf.insert_objects(self.original_graph.nodes())
	
	for node in self.original_graph.nodes():
		uf.find(node)
	
		for edge in self.sorted_edges:
			if uf.find(edge[0]) != uf.find(edge[1]):
				self.tree.add_edge(edge[0], edge[1])
				uf.union(edge[0], edge[1])
	
	print("\nHere is the MST from the given graph: ")

	for edge in self.tree.edges():
		a=edge[0]
   		b=edge[1]
		print("edge "+str(edge))

	return self.tree
 
 



