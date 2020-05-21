class Matrix:
    def __init__(self, data):
        self.data = data

    def at(self, row, col):
        return self.data[row][col]
