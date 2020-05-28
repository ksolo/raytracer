from data_structures import Coordinates
from drawing.transformations import translation, scaling


class TestTranslation:
    def test_multiplying_translation_matrix(self):
        transform = translation(5, -3, 2)
        point = Coordinates.point(-3, 4, 5)

        result = transform * point

        assert result == Coordinates.point(2, 1, 7)

    def test_multiplying_by_inverse_of_translation_matrix(self):
        transform = translation(5, -3, 2)
        inverse = transform.inverse()
        point = Coordinates.point(-3, 4, 5)

        result = inverse * point

        assert result == Coordinates.point(-8, 7, 3)

    def test_translation_does_not_affect_vectors(self):
        transform = translation(5, -3, 2)
        vector = Coordinates.vector(-3, 4, 5)

        result = transform * vector

        assert result == vector


class TestScaling:
    def test_scaling_matrix_applied_to_point(self):
        transform = scaling(2, 3, 4)
        point = Coordinates.point(-4, 6, 8)

        result = transform * point

        assert result == Coordinates.point(-8, 18, 32)

    def test_scaling_matrix_applied_to_vector(self):
        transform = scaling(2, 3, 4)
        vector = Coordinates.vector(-4, 6, 8)

        result = transform * vector

        assert result == Coordinates.vector(-8, 18, 32)

    def test_multiply_by_inverse_of_scaling_matrix(self):
        transform = scaling(2, 3, 4).inverse()
        vector = Coordinates.vector(-4, 6, 8)

        result = transform * vector

        assert result == Coordinates.vector(-2, 2, 2)

    def test_reflection_is_scaling_by_a_negative_value(self):
        transform = scaling(-1, 1, 1)
        point = Coordinates.point(2, 3, 4)

        result = transform * point

        assert result == Coordinates.point(-2, 3, 4)
