from queue import Queue

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2
        self.parent = None  # Added this line

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def water_jug_problem(capacity_jug1, capacity_jug2, target):
    initial_state = State(0, 0)
    visited = set()
    queue = Queue()

    queue.put(initial_state)
    visited.add(initial_state)

    while not queue.empty():
        current_state = queue.get()

        if current_state.jug1 == target or current_state.jug2 == target:
            print("Solution found:")
            print_path(current_state)
            return

        # Fill jug 1
        fill_jug1 = State(capacity_jug1, current_state.jug2)
        enqueue_state(fill_jug1, visited, queue, current_state)

        # Fill jug 2
        fill_jug2 = State(current_state.jug1, capacity_jug2)
        enqueue_state(fill_jug2, visited, queue, current_state)

        # Empty jug 1
        empty_jug1 = State(0, current_state.jug2)
        enqueue_state(empty_jug1, visited, queue, current_state)

        # Empty jug 2
        empty_jug2 = State(current_state.jug1, 0)
        enqueue_state(empty_jug2, visited, queue, current_state)

        # Pour water from jug 1 to jug 2
        pour_jug1_to_jug2 = State(
            max(0, current_state.jug1 - (capacity_jug2 - current_state.jug2)),
            min(capacity_jug2, current_state.jug2 + current_state.jug1)
        )
        enqueue_state(pour_jug1_to_jug2, visited, queue, current_state)

        # Pour water from jug 2 to jug 1
        pour_jug2_to_jug1 = State(
            min(capacity_jug1, current_state.jug1 + current_state.jug2),
            max(0, current_state.jug2 - (capacity_jug1 - current_state.jug1))
        )
        enqueue_state(pour_jug2_to_jug1, visited, queue, current_state)

    print("No solution found.")

def enqueue_state(new_state, visited, queue, current_state):
    if new_state not in visited:
        queue.put(new_state)
        visited.add(new_state)
        new_state.parent = current_state

def print_path(final_state):
    path = []
    current_state = final_state
    while current_state:
        path.append((current_state.jug1, current_state.jug2))
        current_state = current_state.parent

    for state in reversed(path):
        print(f"Jug 1: {state[0]}, Jug 2: {state[1]}")

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2

    water_jug_problem(jug1_capacity, jug2_capacity, target)
