from functools import reduce

from data_structures import Coordinates


class Matrix:
    def __init__(self, data):
        self.data = data

    def at(self, row, col):
        return self.data[row][col]

    def column(self, col):
        return [row[col] for row in self.data]

    def row(self, row):
        return self.data[row]

    def transpose(self):
        return self.__class__([self.column(i) for i in range(len(self.data[0]))])

    def determinant(self):
        return (self.at(0, 0) * self.at(1, 1)) - (self.at(0, 1) * self.at(1, 0))

    def submatrix(self, rindex, cindex):
        data = [row[:] for i, row in enumerate(self.data) if i != rindex]
        for row in data:
            row.pop(cindex)
        return self.__class__(data)

    def minor(self, rindex, cindex):
        return self.submatrix(rindex, cindex).determinant()

    def cofactor(self, rindex, cindex):
        minor = self.minor(rindex, cindex)
        return minor if (rindex + cindex % 2 == 0) else -minor

    def __eq__(self, other):
        return self.data == other.data

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self._mul_matrix_by_matrix(other)
        elif isinstance(other, Coordinates):
            return self._mul_matrix_by_coordinates(other)

    def _mul_matrix_by_matrix(self, other):
        # colums of `self` must equal rows in other
        if len(self.data[0]) != len(other.data):
            pass

        data = []
        for ri in range(len(self.data)):
            data.append([])
            for ci in range(len(other.data[0])):
                total = reduce(
                    lambda prev, curr: prev + curr[0] * curr[1],
                    zip(self.row(ri), other.column(ci)),
                    0,
                )
                data[ri].append(total)

        return self.__class__(data)

    def _mul_matrix_by_coordinates(self, coord):
        data = []
        for row in self.data:
            total = reduce(
                lambda prev, curr: prev + curr[0] * curr[1], zip(row, coord), 0,
            )
            data.append(total)

        return Coordinates(*data)
