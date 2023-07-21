class Matrix:
    matrix = []
    EMPTY_VALUE = 0
    SET_VALUE = 1
    DEFAULT_WIDTH = 15
    DEFAULT_HEIGHT = 7

    def __init__(self, rows: int = DEFAULT_HEIGHT, columns: int = DEFAULT_WIDTH):
        self.rows = rows
        self.columns = columns
        self.clear()

    def clear(self):
        self.matrix = [[self.EMPTY_VALUE] * self.columns for _ in range(self.rows)]

    def at(self, col: int, row: int):
        return self.matrix[row][col]

    def set(self, col: int, row: int, value: int = SET_VALUE):
        row %= self.rows
        col %= self.columns
        self.matrix[row][col] = value
