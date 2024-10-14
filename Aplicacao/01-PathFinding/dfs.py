# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:18:26 2022

@author: Daniel Nogueira

"""

def dfs(visited, graph, node):
    """
    Parameters
    ----------
    visited : list
        Nó visitados.
    graph : Grafo
        Grafo utilizado.
    node : String
        Nó inicial.

    Returns
    -------
    None.

    """
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited
            
##############################################################################
graph = {
    'V0' : ['V1','V2'],
    'V1' : ['V3', 'V4'],
    'V2' : ['V5'],
    'V3' : [],
    'V4' : ['V5'],
    'V5' : []
}

visited = set() # Set to keep track of visited nodes.

# Driver Code
print("Following is the Depth-First Search")
vv = dfs(visited, graph, node='V0')
print(vv)
