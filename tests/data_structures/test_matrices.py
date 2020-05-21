from data_structures import Matrix


class TestMatrix:
    def test_initialization(self):
        data = [
            [1, 2, 3, 4],
            [5.5, 6.5, 7.5, 8.5],
            [9, 10, 11, 12],
            [13.5, 14.5, 15.5, 16.5],
        ]
        matrix = Matrix(data)

        assert matrix.at(0, 0) == 1
        assert matrix.at(0, 3) == 4
        assert matrix.at(1, 0) == 5.5
        assert matrix.at(1, 2) == 7.5
        assert matrix.at(2, 2) == 11
        assert matrix.at(3, 0) == 13.5
        assert matrix.at(3, 2) == 15.5

    def test_creating_2_by_2_matrix(self):
        data = [[-3, 5], [1, -2]]
        matrix = Matrix(data)

        assert matrix.at(0, 0) == -3
        assert matrix.at(0, 1) == 5
        assert matrix.at(1, 0) == 1
        assert matrix.at(1, 1) == -2

    def test_creating_3_by_3_matrix(self):
        data = [[-3, 5, 0], [1, -2, -7], [0, 1, 1]]
        matrix = Matrix(data)

        assert matrix.at(0, 0) == -3
        assert matrix.at(1, 1) == -2
        assert matrix.at(2, 1) == 1
