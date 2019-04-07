import networkx as nx

from sklearn.neighbors import radius_neighbors_graph
from scipy.sparse import find

import random
import numpy as np
import math
import matplotlib.pyplot as plt


class interval():
    def __init__(self,_a,_b):
         self.a=_a
         self.b=_b

def epsilon_neighborhood_graph(pointcloud,alpha):
     
    mat= radius_neighbors_graph(pointcloud,alpha, mode='distance', include_self=False,p = 2)
    (row,col,entries)=find(mat)
    G =nx.Graph()     
    for i in range(0,len(pointcloud)):
 
        G.add_node(i)
    for i in range(0,len(row)):

        G.add_edge(row[i],col[i],weight=entries[i])
         
    return G 

def epsilon_graph_clusters(pointcloud,alpha):
    
    graph=epsilon_neighborhood_graph(pointcloud,alpha)
    
    CC_graphs=list(nx.connected_component_subgraphs(graph))
    
    CC_points=[]
     
    for CC in CC_graphs:
   
        CC_points.append([pointcloud[i] for i in CC.nodes()])
    return tuple(CC_points)    


def circle_example(number):


    X=[]
    for i in range(0,number):
        angle = random.uniform(0,1)*(math.pi*2)
        x=math.cos(angle)
        y=math.sin(angle)
        X.append((x,y))
      
    return X   


def build_coordiante_filter(X,coordinate): 

    f={}
    for x in X:
        
        f[x]=x[1] 
     
    return f 

  
def calculate_cover(INTERVAL,N,epsilon):  
	Intervals = []
	div = abs(float((INTERVAL[1] - INTERVAL[0])) / N)
	epsilon /= 2
	
	i = float(INTERVAL[0])
    
	while 1:
		next = i + div
		if i == INTERVAL[0]:
			Intervals.append([i, next+epsilon])
		elif next >= INTERVAL[1]:
			Intervals.append([i - epsilon, INTERVAL[1]])
			break;
		else:
			Intervals.append([i - epsilon, next + epsilon])
		i += div
	return Intervals
   

    
def mapper_graph(X,f,N,epsilon,alpha):
		a = min(f, key = f.get)[1]
		b = max(f, key = f.get)[1]
		interval = [a,b]
		U = calculate_cover(interval, N, epsilon)
		V = []
		
		for u in U:
			v = []
			for x in f:
				if f[x] >= u[0] and f[x] <= u[1]:
					v.append(x)	
			V.append(v)
		
		ALL_CLUSTERS = []

		for v in V:
			if len(v) > 0:
				clusters = epsilon_graph_clusters(v, alpha)
				for c in clusters:
					ALL_CLUSTERS.append(c)
			
		G = nx.Graph()
		i = 0
		for c in ALL_CLUSTERS:
			G.add_node(i)
			i+=1
			

		
		i = 0
		for ci in ALL_CLUSTERS:
			j = 0
			for cj in ALL_CLUSTERS:
				inter = set(ci).intersection(cj)
				if len(inter) > 0:
					G.add_edge(i,j)
				j += 1
			i += 1

		return G
          

# define the data
num = 1000
X=circle_example(num)

# define the function f
f=build_coordiante_filter(X,1) 

# params                       
                         
N=5
epsilon=0.15 
alpha=0.15                     

# run the Mapper constructoin
G=mapper_graph(X,f,N,epsilon,alpha)

# draw the grpah
print 'Epsilon: ', epsilon
print 'Alpha: ', alpha
print 'N: ', N
print 'Number of unit circle samples: ', num
nx.draw(G)

plt.show()


    
