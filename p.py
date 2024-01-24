# PROBLEMA DE LAS N-REINAS
# Creamos una clase que se va a llamar solución
class QueensProblem:

    # Constructor de nuestra clase donde sPoint = Punto de inicio (columna y fila), nQueens = Número de Reinas y board para el arreglo del tablero
    def __init__(self, sPointCol, sPointRow, nQueens):
        self.sPointCol = sPointCol
        self.sPointRow = sPointRow
        self.nQueens = nQueens

        # En este arreglo, el índice representa la fila del tablero y el valor en cada índice representa la columna donde se coloca una reina
        # Inicialmente, todos los valores son -1, lo que indica que aún no se ha colocado ninguna reina en esa fila
        self.board = [-1] * nQueens

    # Metodo para validar que la reina no este en una posición invalida
    def validatePoint(self, row, col):
        for i in range(row):
            
            # validar que no este en la misma columna, fila o diagonal
            # si el numero de columna se repite en algun
            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row): 
                return False
        return True
    

    def solveQueens(self, row):
        if row >= self.nQueens:
            return True

        for col in range(self.nQueens):
            self.board[row] = col
            if self.validatePoint(row, col):
                if self.solveQueens(row + 1):
                    return True
            self.board[row] = -1

        return False
    
    # Método para probar que los puntos iniciales no sean mayores al numero de reinas o que no sean menores a cero
    def testVariables(self):
        # Condición
        if (self.sPointCol >= self.nQueens or self.sPointRow >= self.nQueens) or (self.sPointCol < 0 or self.sPointRow < 0):
            # Se llama al error con un mensaje
            raise ValueError('Las posiciones iniciales están incorrectas. Intenta usar un número menor al número de reinas y mayor a cero.')
        
    # Este método 
    def startSol(self):
        # Se llama al método testVariables
        self.testVariables()

        
        if self.sPointRow > 0:
            if not self.solveQueens(0):
                return "No se encontro una solución"

        # Se agrega la reina en el punto inicial
        self.board[self.sPointRow] = self.sPointCol

        # Se llama a la funcion solveQueens
        if not self.solveQueens(self.sPointRow + 1):
            return "No se encontro una solución"

        return self.board
    
    # Método que imprime nuestra solucion con puntos (.) y reinas (Q)
    def printSolution(self):

        # Se llama al método startSol y se le asigna a la variable solution
        solution = self.startSol()
        if isinstance(solution, str):
            print(solution)
        else:
            for row in solution:
                print(" ".join("Q" if col == row else "." for col in range(self.nQueens)))

# Example usage
nQueens = int(input("Ingresa el número de reinas: "))
sPointCol = int(input("Ingresa el numero de columna donde va a estar la primera reina: "))
sPointRow = int(input("Ingresa el numero de fila donde va a estar la primera reina: "))

queens_problem = QueensProblem(sPointCol, sPointRow, nQueens)
queens_problem.printSolution()
