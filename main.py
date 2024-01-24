def validation(solution, k):
    for i in range(k):
        if solution[i] == solution[k] or abs(solution[i] - solution[k]) == abs(i - k):
            return False
    return True

def nQueens(solution, stage, n):
    if stage >= n:
        return True

    for i in range(n):
        solution[stage] = i
        if validation(solution, stage):
            if nQueens(solution, stage + 1, n):
                return True

    return False

def solveNQueens(n, start_row, start_col):
    solution = [-1] * n

    # Validate the start position
    if start_row < 0 or start_row >= n or start_col < 0 or start_col >= n:
        return "Invalid starting position"

    # Place the first queen at the specified starting position
    solution[start_row] = start_col

    # Validate the starting position with respect to other queens
    if not validation(solution, start_row):
        return "Invalid starting position"

    # Start solving from the next row
    if nQueens(solution, start_row + 1, n):
        return solution
    else:
        return "No solution found"


# Example usage
n = 5
start_row = int(input(f"Enter the starting row (0 to {n-1}): "))
start_col = int(input(f"Enter the starting column (0 to {n-1}): "))
print(solveNQueens(n, start_row, start_col))