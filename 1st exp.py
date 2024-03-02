import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None, depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def generate_moves(state):
    moves = []
    blank_i, blank_j = find_blank(state.board)

    if blank_i > 0:
        moves.append(('UP', (blank_i - 1, blank_j)))
    if blank_i < 2:
        moves.append(('DOWN', (blank_i + 1, blank_j)))
    if blank_j > 0:
        moves.append(('LEFT', (blank_i, blank_j - 1)))
    if blank_j < 2:
        moves.append(('RIGHT', (blank_i, blank_j + 1)))

    return moves

def apply_move(board, move):
    new_board = [row.copy() for row in board]
    (i, j), (new_i, new_j) = find_blank(board), move[1]
    new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
    return new_board

def calculate_cost(board, goal):
    cost = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal[i][j]:
                cost += 1
    return cost

def solve_puzzle(initial_state, goal_state):
    heap = [initial_state]
    visited = set()

    while heap:
        current_state = heapq.heappop(heap)

        if current_state.board == goal_state:
            path = []
            while current_state:
                path.append((current_state.move, current_state.board))
                current_state = current_state.parent
            path.reverse()
            return path

        visited.add(tuple(map(tuple, current_state.board)))

        for move in generate_moves(current_state):
            new_board = apply_move(current_state.board, move)
            new_state = PuzzleState(new_board, current_state, move[0], current_state.depth + 1,
                                    current_state.depth + 1 + calculate_cost(new_board, goal_state))

            if tuple(map(tuple, new_state.board)) not in visited:
                heapq.heappush(heap, new_state)

    return None

if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    goal_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]

    initial_state = PuzzleState(initial_board)
    goal_state = goal_board

    solution_path = solve_puzzle(initial_state, goal_state)

    if solution_path:
        for step, board in solution_path:
            print(f"Move: {step}")
            print_board(board)
    else:
        print("No solution found.")
