import networkx as nx
import matplotlib.pyplot as plt


def create_city_transport_network():
    """Створити граф транспортної мережі міста"""
    G = nx.Graph()

    stops = [
        "Central Station", "City Hall", "Shopping Mall", "University",
        "Hospital", "Park", "Sports Center", "Airport", "Beach",
        "Industrial Zone"
    ]
    G.add_nodes_from(stops)

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
    """Візуалізувати граф"""
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                           node_size=1000, alpha=0.6)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("City Transport Network")
    plt.axis('off')
    plt.show()


def analyze_graph(G):
    """Аналіз графа"""
    print("\nGraph Analysis:")
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    print("Degrees:")
    for node in G.nodes:
        print(f"{node}: {G.degree(node)}")
    avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
    print(f"Average degree: {avg_degree}")
    print("Is connected:", nx.is_connected(G))
