from graph_utils import create_city_transport_network, visualize_graph, analyze_graph
from algorithms import dfs_path, bfs_path, dijkstra_shortest_paths


def main():
    # Завдання 1: Створення і візуалізація графа
    G = create_city_transport_network()
    visualize_graph(G)
    analyze_graph(G)

    # Завдання 2: DFS і BFS
    start_node = "Central Station"
    end_node = "Beach"

    print(f"\nFinding path from {start_node} to {end_node}:")

    dfs_result = dfs_path(G, start_node, end_node)
    bfs_result = bfs_path(G, start_node, end_node)

    print(f"DFS path: {' -> '.join(dfs_result)}")
    print(f"BFS path: {' -> '.join(bfs_result)}")

    # Пояснення різниці
    if dfs_result != bfs_result:
        print("\n❗ DFS і BFS повернули різні шляхи.")
        print("DFS шукає в глибину, може знайти довший або не найефективніший шлях.")
        print("BFS шукає в ширину, тому завжди знаходить найкоротший (за кількістю кроків) шлях у невагомому графі.")

    # Завдання 3: Найкоротші шляхи — Дейкстра
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
