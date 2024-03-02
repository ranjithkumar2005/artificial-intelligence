from itertools import permutations

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i+1]]
    total_distance += distances[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    cities = len(distances)
    if cities < 2:
        print("Not enough cities for the problem.")
        return

    # Generate all possible orderings of cities
    all_permutations = permutations(range(cities))

    min_distance = float('inf')
    optimal_order = None

    for order in all_permutations:
        total_distance = calculate_total_distance(order, distances)

        if total_distance < min_distance:
            min_distance = total_distance
            optimal_order = order

    return optimal_order, min_distance

if __name__ == "__main__":
    # Example distances between cities (symmetric matrix)
    example_distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    optimal_order, min_distance = traveling_salesman_bruteforce(example_distances)

    print("Optimal order:", optimal_order)
    print("Minimum distance:", min_distance)
