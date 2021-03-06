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

    def test_matrix_is_invertible(self):
        matrix = Matrix([[6, 4, 4, 4], [5, 5, 7, 6], [4, -9, 3, -7], [9, 1, 7, -6]])
        assert matrix.is_invertible()

    def test_matrix_is_not_invertible(self):
        matrix = Matrix([[-4, 2, -2, -3], [9, 6, 2, 6], [0, -5, 1, -5], [0, 0, 0, 0]])
        assert not matrix.is_invertible()

    def test_inverse_matrix(self):
        matrix = Matrix([[-5, 2, 6, -8], [1, -5, 1, 8], [7, 7, -6, -7], [1, -3, 7, 4]])

        result = matrix.inverse()

        assert matrix.determinant() == 532
        assert matrix.cofactor(2, 3) == -160
        assert matrix.cofactor(3, 2) == 105

        assert result.at(3, 2) == -160 / 532
        assert result.at(2, 3) == 105 / 532
        assert self.rounded(result.data) == [
            [0.21805, 0.45113, 0.24060, -0.04511],
            [-0.80827, -1.45677, -0.44361, 0.52068],
            [-0.07895, -0.22368, -0.05263, 0.19737],
            [-0.52256, -0.81391, -0.30075, 0.30639],
        ]

    def test_second_4_by_4_inversion(self):
        matrix = Matrix([[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]])

        result = matrix.inverse()

        assert self.rounded(result.data) == [
            [-0.15385, -0.15385, -0.28205, -0.53846],
            [-0.07692, 0.12308, 0.02564, 0.03077],
            [0.35897, 0.35897, 0.43590, 0.92308],
            [-0.69231, -0.69231, -0.76923, -1.92308],
        ]

    def test_inversion_reverts_correctly(self):
        m1 = Matrix([[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]])
        m2 = Matrix([[8, 2, 2, 2], [3, -1, 7, 0], [7, 0, 5, 4], [6, -2, 0, 5]])
        m3 = m1 * m2

        result = m3 * m2.inverse()

        assert self.rounded(m1.data) == self.rounded(result.data)

    def rounded(self, dataset):
        """helper method to round expected values"""
        data = []
        for row in dataset:
            data.append([round(val, 5) for val in row])
        return data
