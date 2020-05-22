class Matrix:
    def __init__(self, data):
        self.data = data

    def at(self, row, col):
        return self.data[row][col]

    def column(self, col):
        return [row[col] for row in self.data]

    def row(self, row):
        return self.data[row]

    def __eq__(self, other):
        return self.data == other.data

    def __mul__(self, other):
        # colums of `self` must equal rows in other
        if len(self.data[0]) != len(other.data):
            pass

        data = []
        for ri in range(len(self.data)):
            data.append([])
            for ci in range(len(other.data[0])):
                row = self.row(ri)
                col = other.column(ci)

                total = 0
                for i in range(len(row)):
                    total += row[i] * col[i]

                data[ri].append(total)

        return self.__class__(data)
