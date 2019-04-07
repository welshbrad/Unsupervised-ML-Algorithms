# -*- coding: utf-8 -*-

import networkx as nx
from unionfind import *
# Load a graph example from networkx 

graph=nx.house_x_graph()

print("The nodes of the graph are given by the list : ")

print(graph.nodes())


print("The edges of the graph are given by the list : ")

print(graph.edges())

# here we are giving weights to the edges
initweight=1
for edge in graph.edges():
    graph.add_edge(edge[0], edge[1], weight=initweight)
    initweight=initweight+1

# check the weights of the edges:
    
for edge in graph.edges():
    a=edge[0]
    b=edge[1]
    print("edge "+str(edge)+" has  weight " + str(graph[a][b]['weight']) )
 
    
   

 
