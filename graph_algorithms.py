#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import networkx as nx
import networkx.algorithms.tree as tree
import community as community_louvain
import matplotlib.cm as cm
import operator
import numpy as np
import csv 
import sys
import pandas as pd
import csv


# In[2]:


csv_reader = pd.read_csv('person_knows_person.csv', sep="|" , header = None)
csv_reader.to_csv(r'./person_knows_person.txt', header = None, index=None, sep=' ', mode='a')
g = nx.read_edgelist('./person_knows_person.txt', create_using = nx.Graph(), nodetype = int)
print(nx.info(g))


# In[3]:


nodelist = list(g.nodes)
graph  = nx.draw(g, node_color="cyan", with_labels = True)
plt.show()


# In[4]:


##### Q1) Dijkstra and A* to find the shortest path in the graph 
dp=[nx.dijkstra_path(g,38,k, weight =1) for k in nodelist] # shortest path using dijkstra
print(dp)


# In[5]:


ap = [nx.astar_path(g,38,k, weight =1) for k in nodelist] # shortest path using A* star algorithm
print(ap) 


# In[6]:


##### Q2) Prim and Kruskal to find the MST
# Prim Algorithm
prim = tree.minimum_spanning_tree(g, algorithm='prim')
sorted(prim.edges(data=True))


# In[7]:


# Kruskal Algorithm
krusk = tree.minimum_spanning_tree(g, algorithm='kruskal')
sorted(krusk.edges(data=True))


# In[8]:


##### Q3) Page rank and HITS algorithm to order the graph nodes based on their importance
## Page Rank
pr = nx.pagerank(g, alpha = 0.9)
sorted_d = dict( sorted(pr.items(), key=operator.itemgetter(1),reverse=True))
print('Page rank order of nodes based on the order of their importance : ',sorted_d)
nodes = list(sorted_d.keys())
print( 'Page ranked nodes based on the order of their importance : ', nodes)


# In[9]:


## HITS
hits = nx.hits(g, max_iter = 100, normalized = True) 
h,a = hits

sorted_h = dict( sorted(h.items(), key=operator.itemgetter(1),reverse=True))
print('HIT order of nodes based on the order of their importance using hub score :\n ',sorted_h) 
nodes_h = list(sorted_h.keys())
print( '\n HIT based on the order of their importance using hub score:\n ', nodes_h)

sorted_a = dict( sorted(a.items(), key=operator.itemgetter(1),reverse=True))
print('\n HIT order of nodes based on the order of their importance using authority score:\n ',sorted_a) 
nodes_a = list(sorted_a.keys())
print( '\n HIT based on the order of their importance using authority score:\n ', nodes_a)


# In[10]:


##### Q4) Louvain or Leiden for community detection and visualize the result
###Louvain
node_size = []
l = list(sorted_d.values())
for i in l:
    node_size.append((i*4000) + 25)
partition = community_louvain.best_partition(g)
print(partition)
# visualization
pos = nx.spring_layout(g)
cmap = cm.get_cmap('spring', max(partition.values()) + 1)
nx.draw_networkx_nodes(g, pos, partition.keys(), node_size=node_size ,cmap=cmap,node_color=list(partition.values()))
nx.draw_networkx_edges(g, pos, alpha=0.8)
plt.show()


# In[ ]:




