class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)

        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    # Example graph
    example_graph = Graph()
    example_graph.add_edge(1, [2, 3])
    example_graph.add_edge(2, [1, 4, 5])
    example_graph.add_edge(3, [1, 6])
    example_graph.add_edge(4, [2])
    example_graph.add_edge(5, [2, 7])
    example_graph.add_edge(6, [3])
    example_graph.add_edge(7, [5])

    start_node = 1

    print(f"DFS traversal starting from node {start_node}:")
    visited_nodes = set()
    dfs(example_graph.graph, start_node, visited_nodes)
