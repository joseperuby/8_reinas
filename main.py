# PROBLEMA DE LAS N-REINAS

# Definimos una clase para resolver el problema de las N-Reinas.
class QueensProblem:

     # Constructor de la clase con los parámetros de inicio y el número de reinas.
    def __init__(self, sPointCol, sPointRow, nQueens):
        self.sPointCol = sPointCol  # Columna inicial de una reina.
        self.sPointRow = sPointRow  # Fila inicial de una reina.
        self.nQueens = nQueens      # Total de reinas.

         # Creamos un arreglo para el tablero donde cada índice es una fila y el valor es la columna de la reina.
        self.board = [-1] * nQueens # Inicializamos todas las posiciones con -1, indicando que no hay reinas colocadas.

    # Verifica si una reina puede ser colocada en una fila y columna dada sin conflictos.
    def validatePoint(self, row, col):
        for i in range(row):
            # Comprueba si hay conflictos en filas o diagonales.
            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    # Intenta resolver el problema colocando reinas columna por columna.
    def solveQueens(self, row):
        if row >= self.nQueens: 
            return True  # Todas las reinas están colocadas correctamente.

        for col in range(self.nQueens):
            if row == self.sPointRow and col != self.sPointCol: # Condicion para la posicion inicial
                continue  # Se omite estan fila para ya no tener que buscar mas en la fila de la posicion inicial
            self.board[row] = col # Colocamos una reina (siempre vamos a empezar en 0,0)
            if self.validatePoint(row, col):
                if self.solveQueens(row + 1):
                    return True
            if row != self.sPointRow:
                self.board[row] = -1  # Elimina la reina si no es posible colocarla.

        return False

    # Verifica si las posiciones iniciales son válidas.
    def testVariables(self):
        if (self.sPointCol >= self.nQueens or self.sPointRow >= self.nQueens) or (self.sPointCol < 0 or self.sPointRow < 0):
            raise ValueError('Las posiciones iniciales están incorrectas.')

    # Inicia la solución del problema.
    def startSol(self):
        self.testVariables()
        self.board[self.sPointRow] = self.sPointCol # Se coloca la reina inicial.
        if not self.solveQueens(0): # Se llama al metodo solveQueens para ir resolviendo el problema iniciando desde la primera fila y primera columna.
            return "No se encontró una solución"
        return self.board

    # Imprime la solución al problema.
    def printSolution(self):
        solution = self.startSol()
        if isinstance(solution, str): # Si solucion es un string imprime ese string
            print(solution)
        else:
            # Imprimimos el tablero con las reinas (Q) y espacios vacíos (.)
            for row in solution:
                print(" ".join("Q" if col == row else "." for col in range(self.nQueens)))

# Pedir variables
nQueens = int(input("Ingresa el número de reinas: "))
sPointCol = int(input("Ingresa el número de columna donde va a estar la primera reina: "))
sPointRow = int(input("Ingresa el número de fila donde va a estar la primera reina: "))

# Crea una instancia del problema e llamamos al metodo para imprimir la solución.
queens_problem = QueensProblem(sPointCol, sPointRow, nQueens)
queens_problem.printSolution()
