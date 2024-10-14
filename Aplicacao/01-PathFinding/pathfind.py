import heapq
import time
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append((destination, weight))

class SearchResult:
    def __init__(self, path, nodes_visited, execution_time):
        self.path = path
        self.nodes_visited = nodes_visited
        self.execution_time = execution_time

def a_star(graph, start, goal, heuristic):
    start_time = time.time()
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}
    nodes_visited = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        nodes_visited += 1

        if current == goal:
            end_time = time.time()
            return SearchResult(reconstruct_path(came_from, current), nodes_visited, end_time - start_time)

        for neighbor, weight in graph.adjacency_list[current]:
            tentative_g_score = g_score[current] + weight
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    end_time = time.time()
    return SearchResult([], nodes_visited, end_time - start_time)

def dijkstra(graph, start, goal):
    start_time = time.time()
    
    # Inicializa todas as distâncias como infinito para todos os nós
    distances = {vertex: float('infinity') for vertex in graph.adjacency_list}
    
    # Certifica-se de incluir todos os destinos no dicionário de distâncias
    for neighbors in graph.adjacency_list.values():
        for neighbor, _ in neighbors:
            if neighbor not in distances:
                distances[neighbor] = float('infinity')
    
    distances[start] = 0
    previous_nodes = {}
    nodes = [(0, start)]
    nodes_visited = 0

    while nodes:
        current_distance, current_vertex = heapq.heappop(nodes)
        nodes_visited += 1

        if current_vertex == goal:
            end_time = time.time()
            return SearchResult(reconstruct_path(previous_nodes, current_vertex), nodes_visited, end_time - start_time)

        for neighbor, weight in graph.adjacency_list[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(nodes, (distance, neighbor))

    end_time = time.time()
    return SearchResult([], nodes_visited, end_time - start_time)


def dfs(graph, start, goal):
    start_time = time.time()
    stack = [start]
    visited = set()
    came_from = {}
    nodes_visited = 0

    while stack:
        current = stack.pop()
        nodes_visited += 1

        if current == goal:
            end_time = time.time()
            return SearchResult(reconstruct_path(came_from, current), nodes_visited, end_time - start_time)

        if current not in visited:
            visited.add(current)
            for neighbor, _ in graph.adjacency_list[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    came_from[neighbor] = current

    end_time = time.time()
    return SearchResult([], nodes_visited, end_time - start_time)

def bfs(graph, start, goal):
    start_time = time.time()
    queue = deque([start])
    visited = set()
    came_from = {}
    nodes_visited = 0

    while queue:
        current = queue.popleft()
        nodes_visited += 1

        if current == goal:
            end_time = time.time()
            return SearchResult(reconstruct_path(came_from, current), nodes_visited, end_time - start_time)

        if current not in visited:
            visited.add(current)
            for neighbor, _ in graph.adjacency_list[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    came_from[neighbor] = current

    end_time = time.time()
    return SearchResult([], nodes_visited, end_time - start_time)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def print_result(result):
    print(f"Path: {' -> '.join(map(str, result.path))}")
    print(f"Nodes Visited: {result.nodes_visited}")
    print(f"Execution Time: {result.execution_time * 1000:.2f} ms\n")


def main():
    graph = Graph()
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 4)
    graph.add_edge(2, 3, 2)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 1)

    start = 1
    goal = 4

    heuristic = lambda node: abs(node - goal)

    a_star_result = a_star(graph, start, goal, heuristic)
    dijkstra_result = dijkstra(graph, start, goal)
    dfs_result = dfs(graph, start, goal)
    bfs_result = bfs(graph, start, goal)

    print("A* Search:")
    print_result(a_star_result)
    print("Dijkstra's Algorithm:")
    print_result(dijkstra_result)
    print("Depth-First Search (DFS):")
    print_result(dfs_result)
    print("Breadth-First Search (BFS):")
    print_result(bfs_result)


if __name__ == "__main__":
    main()
