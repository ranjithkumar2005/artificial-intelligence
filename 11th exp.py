def is_valid_assignment(assignment, node, color):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(assignment):
    if len(assignment) == len(graph):
        return assignment

    node = select_unassigned_variable(assignment)
    for color in colors:
        if is_valid_assignment(assignment, node, color):
            assignment[node] = color
            result = backtracking(assignment)
            if result:
                return result
            del assignment[node]

    return None

def select_unassigned_variable(assignment):
    for node in graph:
        if node not in assignment:
            return node

if __name__ == "__main__":
    # Example map graph (graph represented as an adjacency list)
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }

    # Colors available for coloring
    colors = ['Red', 'Green', 'Blue']

    # Perform backtracking to find a valid coloring
    assignment = backtracking({})
    
    if assignment:
        print("Valid Map Coloring:")
        for node, color in assignment.items():
            print(f"{node}: {color}")
    else:
        print("No valid coloring found.")
