import numpy as np
import unionfind as unionfind
import networkx as nx

'''
Part 1, 0-barcode
'''

# this function is provided to you in case you want to load the data sets I gave to you.
def load_data_from_hd(path): # path must be a string to the location of the file
    
    with open(path) as f:
        names_list = [line.split(',') for line in f if line.strip()]
    f=[]    
    for line in names_list:
        f.append([float(x) for x in line])
    return np.array(f)


def zero_barcode_pointcloud(dist_matrix, alpha):
	#create e-neighborhood graph from matrix
	complete_graph = nx.from_numpy_matrix(dist_matrix)
	G_epsilon = nx.Graph()
	
	for node in complete_graph.nodes():
		G_epsilon.add_node(node)
		
	for edge in complete_graph.edges():
		weight = complete_graph[edge[0]][edge[1]]['weight']
		if weight <= alpha:
			G_epsilon.add_edge(edge[0],edge[1], weight = weight)
	
	#init unionFind		
	U = unionfind.UnionFind()
	#init bars
	bars = []
	
	#for each node in graph, create a set, and create a default bar
	for vi in G_epsilon.nodes():
		U.find(vi)
		bars.append([0, float("inf")])


	#sort edges by weights (increasing)
	edges = sorted(G_epsilon.edges(data=True), key=lambda x: x[2]['weight'])
	

	for edge in edges:
		if U.find(edge[0]) != U.find(edge[1]):
			U.union(edge[0], edge[1])
			bars[edge[0]][1] = G_epsilon[edge[0]][edge[1]]['weight']

	return bars
	
#Part 1 test
M = np.matrix([[0.0, 3.5, 4.5, 7.0],
               [3.5, 0.0, 9.0, 2.1],
               [4.5, 9.0, 0.0, 1.0],
               [7.0, 2.1, 1.0, 0.0]],dtype=[('weight',float)])
epsilon = 9;

print("Testing Part 1.....")
print("Bars [Born, Dead]:")
bars = zero_barcode_pointcloud(M, epsilon)
for bar in bars:
	print(bar)


'''
Part2

Bradley Welsh, HW4

The data set 1 and 2 both probably have one uniformly-connected component after a threshold epsilon because there is one highly persistent 
0-dimensional bar and a lot of relatively low-persistent bars

Data set 1 has a 1-dimensional persistent feature that shows a hole that persists for a long time, which means the data is highly circular.
Persistence of this feature is about 1.35


Data set 2 has two long persistent 1-dimensional bars that persist at roughly the same epsilon which means the data homologically similar to a taurus (both have persistence of about 1.25)


'''





"""

Part 3 (Bonus)scalar function 0-barcode 

"""

# use the following dataset as an input for this function

pointcloud=[(1,1),(2,2),(3,4),(4,3),(5,5),(6,3.5),(7,7),(8,8),(9,9),(10,8),(11,9.5),(11,7.5),(12,12),(13,1.5)]



def zero_barcode_scalar_functoin(pointcloud,alpha):
    return

