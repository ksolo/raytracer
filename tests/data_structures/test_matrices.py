from data_structures import Coordinates
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

    def test_equality_with_equal_data_sets(self):
        data1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
        data2 = data1[::]

        m1 = Matrix(data1)
        m2 = Matrix(data2)

        assert m1 == m2

    def test_not_equal_with_non_equal_data_sets(self):
        data1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
        data2 = [[3, 2, 3, 4], [4, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]

        m1 = Matrix(data1)
        m2 = Matrix(data2)

        assert m1 != m2

    def test_matrix_multiplication(self):
        m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        m2 = Matrix([[-2, 1, 2, 3], [3, 2, 1, -1], [4, 3, 6, 5], [1, 2, 7, 8]])

        result = m1 * m2

        assert result == Matrix(
            [[20, 22, 50, 48], [44, 54, 114, 108], [40, 58, 110, 102], [16, 26, 46, 42]]
        )

    def test_matrix_multiplication_to_coordinate(self):
        matrix = Matrix([[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]])
        coord = Coordinates(1, 2, 3, 1)

        result = matrix * coord

        assert result == Coordinates(18, 24, 33, 1)

    def test_matrix_mul_by_identity_matrix(self):
        m = Matrix([[0, 1, 2, 4], [1, 2, 4, 8], [2, 4, 8, 16], [4, 8, 16, 32]])
        identity_matrix = Matrix(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        )

        result = m * identity_matrix

        assert result == m

    def test_idenity_matrix_mul_by_coordinates(self):
        identity_matrix = Matrix(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        )
        coord = Coordinates(1, 2, 3, 4)

        result = identity_matrix * coord

        assert result == coord

    def test_transposing_matrix(self):
        m = Matrix([[0, 9, 3, 0], [9, 8, 0, 8], [1, 8, 5, 3], [0, 0, 5, 8]])

        result = m.transpose()

        assert result == Matrix(
            [[0, 9, 1, 0], [9, 8, 8, 0], [3, 0, 5, 5], [0, 8, 3, 8]]
        )

    def test_transposing_identity_matrix_results_in_identity_matrix(self):
        identity_matrix = Matrix(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        )

        result = identity_matrix.transpose()

        assert result == identity_matrix

    def test_calculating_determinant_of_2_by_2_matrix(self):
        matrix = Matrix([[1, 5], [-3, 2]])

        result = matrix.determinant()

        assert result == 17

    def test_submatrix_of_3_by_3_is_2_by_2_matrix(self):
        matrix = Matrix([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])

        result = matrix.submatrix(0, 2)

        assert result == Matrix([[-3, 2], [0, 6]])

    def test_submatrix_of_4_by_4_matrix_is_3_by_3_matrix(self):
        matrix = Matrix([[-6, 1, 1, 6], [-8, 5, 8, 6], [-1, 0, 8, 2], [-7, 1, -1, 1]])

        result = matrix.submatrix(2, 1)

        assert result == Matrix([[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])

    def test_caclculating_minor_of_3_by_3_matrix(self):
        matrix = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
        sub_matrix = matrix.submatrix(1, 0)

        determinant = sub_matrix.determinant()
        minor = matrix.minor(1, 0)

        assert determinant == 25
        assert determinant == minor

    def test_calculating_cofactor_of_3_by_3_matrix(self):
        matrix = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])

        assert matrix.minor(0, 0) == -12
        assert matrix.minor(0, 0) == matrix.cofactor(0, 0)

        assert matrix.minor(1, 0) == 25
        assert matrix.cofactor(1, 0) == -25

    def test_calculating_determinant_of_3_by_3_matrix(self):
        matrix = Matrix([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])

        assert matrix.cofactor(0, 0) == 56
        assert matrix.cofactor(0, 1) == 12
        assert matrix.cofactor(0, 2) == -46
        assert matrix.determinant() == -196

    def test_calculating_determinant_of_4_by_4_matrix(self):
        matrix = Matrix([[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]])

        assert matrix.cofactor(0, 0) == 690
        assert matrix.cofactor(0, 1) == 447
        assert matrix.cofactor(0, 2) == 210
        assert matrix.cofactor(0, 3) == 51
        assert matrix.determinant() == -4071
