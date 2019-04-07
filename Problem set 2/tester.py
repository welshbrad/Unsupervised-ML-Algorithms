import zahn_algorithm as zahn
import kruskalsalgorithm as ka
import BFS_graph_connected_components as BFS
import EMST as EMST
import epsilon_graph as eps
import networkx as nx

X = [[1, 10], [200, 4], [3, 7], [5,70], [4,4], [310, 900], [0,0], [40,100], [210,1000]] #test data -- points
e = 5 #used for epsilon neighborhood graph and clustering
k = 2 #used for Zahn's algorithm, k = number of clusters
G = nx.Graph(X) #graph from test data



print("==============Testing BFS===============")
print(BFS.BFS(G))
print("\n==============Testing EMST==============")
EMST.EMST(X)
print("\n============Testing Zahn's Algorithm==============")
zahn.zahn_algorithm(X, k)
print("\n============Testing e-neighborhood graph clustering==============")
print "\nNeighborhood graph: \n", eps.epsilon_graph(X,e) 
print "\nConnected components: \n", str(eps.epsilon_graph_clusters(X,e))

