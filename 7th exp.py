from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

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

    print(f"BFS traversal starting from node {start_node}:")
    bfs(example_graph.graph, start_node)
