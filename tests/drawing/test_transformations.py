from math import radians, sqrt

from data_structures import Coordinates
from drawing.transformations import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
)


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


class TestRotation:
    def test_rotating_a_point_around_x_axis(self):
        point = Coordinates.point(0, 1, 0)
        half_quarter = rotation_x(radians(45))
        full_quarter = rotation_x(radians(90))

        half_quarter_rotation = half_quarter * point
        full_quarter_rotaton = full_quarter * point

        assert self.rounded(half_quarter_rotation) == self.rounded(
            [0, sqrt(2) / 2, sqrt(2) / 2, 1]
        )
        assert self.rounded(full_quarter_rotaton) == self.rounded(
            Coordinates.point(0, 0, 1)
        )

    def test_inverse_of_x_rotation_goes_in_opposite_direction(self):
        point = Coordinates.point(0, 1, 0)
        half_quarter = rotation_x(radians(45)).inverse()

        half_quarter_rotation = half_quarter * point

        assert self.rounded(half_quarter_rotation) == self.rounded(
            [0, sqrt(2) / 2, -(sqrt(2) / 2), 1,]
        )

    def test_rotating_a_point_around_y_axis(self):
        point = Coordinates.point(0, 0, 1)
        half_quarter = rotation_y(radians(45))
        full_quarter = rotation_y(radians(90))

        half_quarter_rotation = half_quarter * point
        full_quarter_rotaton = full_quarter * point

        assert self.rounded(half_quarter_rotation) == self.rounded(
            [sqrt(2) / 2, 0, sqrt(2) / 2, 1]
        )
        assert self.rounded(full_quarter_rotaton) == self.rounded([1, 0, 0, 1])

    def test_rotating_a_point_around_z_axis(self):
        point = Coordinates.point(0, 1, 0)
        half_quarter = rotation_z(radians(45))
        full_quarter = rotation_z(radians(90))

        half_quarter_rotation = half_quarter * point
        full_quarter_rotaton = full_quarter * point

        assert self.rounded(half_quarter_rotation) == self.rounded(
            [-sqrt(2) / 2, sqrt(2) / 2, 0, 1]
        )
        assert self.rounded(full_quarter_rotaton) == self.rounded([-1, 0, 0, 1])

    def rounded(self, point):
        return [round(coordinate, 5) for coordinate in point]
