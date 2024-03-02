from queue import Queue

class State:
    def __init__(self, missionaries, cannibals, boat_side):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_side = boat_side

    def __eq__(self, other):
        return (self.missionaries, self.cannibals, self.boat_side) == (other.missionaries, other.cannibals, other.boat_side)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat_side))

def is_valid_state(state):
    if state.missionaries < 0 or state.missionaries > 3 or \
       state.cannibals < 0 or state.cannibals > 3:
        return False

    if state.missionaries < state.cannibals and state.missionaries > 0:
        return False

    if 3 - state.missionaries < 3 - state.cannibals and 3 - state.missionaries > 0:
        return False

    return True

def generate_next_states(current_state):
    next_states = []

    if current_state.boat_side == 'left':
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    else:
        moves = [(-1, 0), (-2, 0), (0, -1), (0, -2), (-1, -1)]

    for move in moves:
        new_state = State(current_state.missionaries + move[0],
                          current_state.cannibals + move[1],
                          'right' if current_state.boat_side == 'left' else 'left')

        if is_valid_state(new_state):
            next_states.append(new_state)

    return next_states

def solve_missionaries_cannibals():
    initial_state = State(3, 3, 'left')
    goal_state = State(0, 0, 'right')

    visited = set()
    queue = Queue()

    queue.put(initial_state)
    visited.add(initial_state)

    while not queue.empty():
        current_state = queue.get()

        if current_state == goal_state:
            print("Solution found:")
            print_path(current_state)
            return

        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.put(next_state)
                visited.add(next_state)

def print_path(final_state):
    path = []
    current_state = final_state
    while current_state:
        path.append((current_state.missionaries, current_state.cannibals, current_state.boat_side))
        current_state = current_state.parent if hasattr(current_state, 'parent') else None

    for state in reversed(path):
        print(f"Missionaries: {state[0]}, Cannibals: {state[1]}, Boat: {state[2]}")

if __name__ == "__main__":
    solve_missionaries_cannibals()
