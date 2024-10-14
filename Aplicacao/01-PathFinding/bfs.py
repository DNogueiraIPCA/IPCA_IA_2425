# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:37:44 2022

@author: Daniel Nogueira

"""

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        
##############################################################################

graph = {
    'V0' : ['V1','V2'],
    'V1' : ['V3', 'V4'],
    'V2' : ['V5'],
    'V3' : [],
    'V4' : ['V5'],
    'V5' : ['V6'],
    'V6' : ['V7'],
    'V7' : ['V8'],
    'V8' : ['V9'],
    'V9' : ['V10'],
    'V10' : ['V11'],
    'V11' : ['V12'],
    'V12' : ['V0']
    
}

visited = [] # List to keep track of visited nodes.
queue = []   # Initialize a queue

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, node='V0')