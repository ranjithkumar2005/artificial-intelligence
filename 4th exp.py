from itertools import permutations

def is_valid_assignment(assignment, equation):
    if assignment[equation[0][0]] == 0 or assignment[equation[1][0]] == 0 or assignment[equation[2][0]] == 0:
        return False
    num1 = int("".join(str(assignment[ch]) for ch in equation[0]))
    num2 = int("".join(str(assignment[ch]) for ch in equation[1]))
    result = int("".join(str(assignment[ch]) for ch in equation[2]))
    return num1 + num2 == result

def solve_cryptarithmetic(equation):
    unique_chars = set(char for word in equation for char in word)
    if len(unique_chars) > 10:
        print("Invalid equation: Too many unique characters.")
        return

    for perm in permutations(range(10), len(unique_chars)):
        assignment = dict(zip(unique_chars, perm))
        if is_valid_assignment(assignment, equation):
            print("Solution found:")
            for word in equation:
                print(word, "=", int("".join(str(assignment[ch]) for ch in word)))
            return

    print("No solution found.")

if __name__ == "__main__":
    # Example Cryptarithmetic problem: SEND + MORE = MONEY
    equation = ['SEND', 'MORE', 'MONEY']
    solve_cryptarithmetic(equation)
