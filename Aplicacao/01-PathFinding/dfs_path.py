# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:59:38 2023

@author: Daniel Nogueira
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

graph = {
    'V0' : set(['V1','V2']),
    'V1' : set(['V2']),
    'V2' : set(['V5']),
    'V3' : set(['V4']),
    'V4' : set(['V2']),
    'V5' : set()
}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

list(dfs_paths(graph, 'V0', 'V5')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
