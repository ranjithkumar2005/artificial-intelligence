import heapq

class Node:
    def __init__(self, row, col, cost, heuristic):
        self.row = row
        self.col = col
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic
        self.parent = None

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def heuristic(node, goal):
    return abs(node.row - goal[0]) + abs(node.col - goal[1])

def is_valid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 1

def astar(grid, start, goal):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    start_node = Node(start[0], start[1], 0, heuristic(Node(start[0], start[1], 0, 0), goal))
    heap = [start_node]
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)

        if (current_node.row, current_node.col) == goal:
            path = [(current_node.row, current_node.col)]
            while current_node.parent:
                current_node = current_node.parent
                path.append((current_node.row, current_node.col))
            return list(reversed(path))

        visited.add((current_node.row, current_node.col))

        for dr, dc in directions:
            new_row, new_col = current_node.row + dr, current_node.col + dc

            if is_valid(new_row, new_col, grid) and (new_row, new_col) not in visited:
                new_cost = current_node.cost + 1
                new_node = Node(new_row, new_col, new_cost, heuristic(Node(new_row, new_col, new_cost, 0), goal))
                new_node.parent = current_node
                heapq.heappush(heap, new_node)

    return None  # No path found

if __name__ == "__main__":
    # Example grid (0 represents walkable, 1 represents obstacle)
    example_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_position = (0, 0)
    goal_position = (4, 4)

    path = astar(example_grid, start_position, goal_position)

    if path:
        print(f"Path from {start_position} to {goal_position}: {path}")
    else:
        print("No path found.")
