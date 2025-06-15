import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def create_city_transport_network():
    """Create a sample city transport network graph"""
    G = nx.Graph()

    # Add nodes (bus stops)
    stops = [
        "Central Station", "City Hall", "Shopping Mall", "University",
        "Hospital", "Park", "Sports Center", "Airport", "Beach",
        "Industrial Zone"
    ]

    G.add_nodes_from(stops)

    # Add edges (routes) with weights (travel time in minutes)
    routes = [
        ("Central Station", "City Hall", 5),
        ("Central Station", "Shopping Mall", 8),
        ("City Hall", "University", 6),
        ("Shopping Mall", "Hospital", 7),
        ("University", "Park", 4),
        ("Hospital", "Sports Center", 9),
        ("Park", "Airport", 12),
        ("Sports Center", "Beach", 10),
        ("Airport", "Industrial Zone", 15),
        ("Beach", "Industrial Zone", 8),
        ("Central Station", "Airport", 20),
        ("City Hall", "Sports Center", 11),
        ("Shopping Mall", "Park", 9),
        ("University", "Beach", 14)
    ]

    G.add_weighted_edges_from(routes)
    return G


def visualize_graph(G):
    """Visualize the graph with node labels and edge weights"""
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                           node_size=1000, alpha=0.6)

    # Draw edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("City Transport Network")
    plt.axis('off')
    plt.show()


def analyze_graph(G):
    """Analyze basic graph characteristics"""
    print("\nGraph Analysis:")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")

    print("\nNode degrees:")
    for node in G.nodes():
        print(f"{node}: {G.degree(node)}")

    print("\nAverage degree:", sum(
        dict(G.degree()).values()) / G.number_of_nodes())
    print("Is connected:", nx.is_connected(G))


def dfs_path(G, start, end):
    """Find path using Depth-First Search"""
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
    """Find path using Breadth-First Search"""
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
    """Find shortest paths between all pairs of nodes using Dijkstra's algorithm"""
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


def main():
    # Create and visualize the graph
    G = create_city_transport_network()
    visualize_graph(G)

    # Analyze the graph
    analyze_graph(G)

    # Test DFS and BFS
    start_node = "Central Station"
    end_node = "Beach"

    print(f"\nFinding path from {start_node} to {end_node}:")

    dfs_result = dfs_path(G, start_node, end_node)
    print(f"DFS path: {' -> '.join(dfs_result)}")

    bfs_result = bfs_path(G, start_node, end_node)
    print(f"BFS path: {' -> '.join(bfs_result)}")

    # Find shortest paths using Dijkstra's algorithm
    print("\nShortest paths using Dijkstra's algorithm:")
    shortest_paths = dijkstra_shortest_paths(G)

    for start in ["Central Station", "City Hall"]:
        for end in ["Beach", "Airport"]:
            if start != end:
                path, distance = shortest_paths[start][end]
                print(f"\nShortest path from {start} to {end}:")
                print(f"Path: {' -> '.join(path)}")
                print(f"Total distance: {distance} minutes")


if __name__ == "__main__":
    main()
