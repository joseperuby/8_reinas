class QueensProblem:
    def __init__(self, sPointCol, sPointRow, nQueens):
        self.sPointCol = sPointCol
        self.sPointRow = sPointRow
        self.nQueens = nQueens
        self.board = [-1] * nQueens

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def solve_queens(self, row):
        if row >= self.nQueens:
            return True

        for col in range(self.nQueens):
            self.board[row] = col
            if self.is_safe(row, col):
                if self.solve_queens(row + 1):
                    return True
            self.board[row] = -1

        return False

    def testVariables(self):
        if self.sPointCol >= self.nQueens or self.sPointRow >= self.nQueens:
            raise ValueError('Las posiciones iniciales están incorrectas. Intenta usar un número menor al número de reinas.')

    def start_solve(self):
        self.testVariables()
        self.board[self.sPointRow] = self.sPointCol

        if not self.is_safe(self.sPointRow, self.sPointCol):
            return "No solution found starting from the given position"

        if self.sPointRow > 0:
            if not self.solve_queens(0):
                return "No solution found"

        if not self.solve_queens(self.sPointRow + 1):
            return "No solution found"

        return self.board

    def print_solution(self):
        solution = self.start_solve()
        if isinstance(solution, str):
            print(solution)
        else:
            for row in solution:
                print(" ".join("Q" if col == row else "." for col in range(self.nQueens)))

# Example usage
nQueens = int(input("Enter the number of queens (N): "))
sPointCol = int(input("Enter the starting column (0 to N-1): "))
sPointRow = int(input("Enter the starting row (0 to N-1): "))


queens_problem = QueensProblem(sPointCol, sPointRow, nQueens)
queens_problem.print_solution()
