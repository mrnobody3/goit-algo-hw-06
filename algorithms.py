import networkx as nx
from collections import deque


def dfs_path(G, start, end):
    """Depth-First Search"""
    visited = set()
    path = []

    def dfs(current):
        visited.add(current)
        path.append(current)
        if current == end:
            return True
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        path.pop()
        return False

    dfs(start)
    return path if end in path else []


def bfs_path(G, start, end):
    """Breadth-First Search"""
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []


def dijkstra_shortest_paths(G):
    """Dijkstra shortest path for all pairs"""
    all_paths = {}
    for start in G.nodes():
        all_paths[start] = {}
        for end in G.nodes():
            if start != end:
                try:
                    path = nx.dijkstra_path(G, start, end, weight='weight')
                    distance = nx.dijkstra_path_length(
                        G, start, end, weight='weight')
                    all_paths[start][end] = (path, distance)
                except nx.NetworkXNoPath:
                    all_paths[start][end] = (None, float('inf'))
    return all_paths
