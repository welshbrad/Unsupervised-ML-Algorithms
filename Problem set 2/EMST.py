import networkx as nx
import kruskalsalgorithm as ka
from math import sqrt
import numpy as np


#Distance between two points
def distance(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def EMST(points):

	print("Euclidean MST using complete graph construction\n ")
	print("Creating graph from point set X")
	print "List of points: ", points
	print "Number of points: ",len(points), "\n"

	#Create a fully connected graph for each point in x
	G = nx.complete_graph(len(points), create_using=None)

	for u,v,d in G.edges(data=True):
		d['weight']=distance(points[u],points[v])
		#print(d['weight'])
		
	mst = ka.kruskalsalgorithm(G)
	return mst.spanningtree()

	


#list of points
#X = [[1, 10], [200, 4], [3, 7], [5,70]]
#EMST(X)
