from math import radians, sqrt

from data_structures import Coordinates
from drawing.transformations import (
    translation,
    scaling,
    shearing,
    rotation_x,
    rotation_y,
    rotation_z,
)


def rounded(point):
    return [round(coordinate, 5) for coordinate in point]


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

        assert rounded(half_quarter_rotation) == rounded(
            [0, sqrt(2) / 2, sqrt(2) / 2, 1]
        )
        assert rounded(full_quarter_rotaton) == rounded(Coordinates.point(0, 0, 1))

    def test_inverse_of_x_rotation_goes_in_opposite_direction(self):
        point = Coordinates.point(0, 1, 0)
        half_quarter = rotation_x(radians(45)).inverse()

        half_quarter_rotation = half_quarter * point

        assert rounded(half_quarter_rotation) == rounded(
            [0, sqrt(2) / 2, -(sqrt(2) / 2), 1,]
        )

    def test_rotating_a_point_around_y_axis(self):
        point = Coordinates.point(0, 0, 1)
        half_quarter = rotation_y(radians(45))
        full_quarter = rotation_y(radians(90))

        half_quarter_rotation = half_quarter * point
        full_quarter_rotaton = full_quarter * point

        assert rounded(half_quarter_rotation) == rounded(
            [sqrt(2) / 2, 0, sqrt(2) / 2, 1]
        )
        assert rounded(full_quarter_rotaton) == rounded([1, 0, 0, 1])

    def test_rotating_a_point_around_z_axis(self):
        point = Coordinates.point(0, 1, 0)
        half_quarter = rotation_z(radians(45))
        full_quarter = rotation_z(radians(90))

        half_quarter_rotation = half_quarter * point
        full_quarter_rotaton = full_quarter * point

        assert rounded(half_quarter_rotation) == rounded(
            [-sqrt(2) / 2, sqrt(2) / 2, 0, 1]
        )
        assert rounded(full_quarter_rotaton) == rounded([-1, 0, 0, 1])

    def rounded(self, point):
        return [round(coordinate, 5) for coordinate in point]


class TestShearing:
    def test_shearing_transformation_moves_x_in_proportion_to_y(self):
        transform = shearing(1, 0, 0, 0, 0, 0)
        point = Coordinates.point(2, 3, 4)

        result = transform * point

        assert result == Coordinates.point(5, 3, 4)

    def test_shearing_transformation_moves_x_in_proportion_to_z(self):
        transform = shearing(0, 1, 0, 0, 0, 0)
        point = Coordinates.point(2, 3, 4)

        result = transform * point

        assert result == Coordinates.point(6, 3, 4)

    def test_shearing_transformation_moves_y_in_proportion_to_x(self):
        transform = shearing(0, 0, 1, 0, 0, 0)
        point = Coordinates.point(2, 3, 4)

        result = transform * point

        assert result == Coordinates.point(2, 5, 4)

    def test_shearing_transformation_moves_y_in_proportion_to_z(self):
        transform = shearing(0, 0, 0, 1, 0, 0)
        point = Coordinates.point(2, 3, 4)

        result = transform * point

        assert result == Coordinates.point(2, 7, 4)

    def test_shearing_transformation_moves_z_in_proportion_to_x(self):
        transform = shearing(0, 0, 0, 0, 1, 0)
        point = Coordinates.point(2, 3, 4)

        result = transform * point

        assert result == Coordinates.point(2, 3, 6)

    def test_shearing_transformation_moves_x_in_proportion_to_z(self):
        transform = shearing(0, 0, 0, 0, 0, 1)
        point = Coordinates.point(2, 3, 4)

        result = transform * point

        assert result == Coordinates.point(2, 3, 7)


class TestApplyingMultileTranslations:
    def test_individual_transformations_are_applied_in_sequence(self):
        point = Coordinates.point(1, 0, 1)
        rotate = rotation_x(radians(90))
        scale = scaling(5, 5, 5)
        translate = translation(10, 5, 7)

        rotated_point = rotate * point
        scaled_point = scale * rotated_point
        translated_point = translate * scaled_point

        assert rounded(rotated_point) == rounded(Coordinates.point(1, -1, 0))
        assert rounded(scaled_point) == rounded(Coordinates.point(5, -5, 0))
        assert translated_point == Coordinates.point(15, 0, 7)

    def test_chaining_transformations_must_be_applied_in_reverse_order(self):
        point = Coordinates.point(1, 0, 1)
        rotate = rotation_x(radians(90))
        scale = scaling(5, 5, 5)
        translate = translation(10, 5, 7)

        transforms = translate * scale * rotate
        result = transforms * point

        assert result == Coordinates.point(15, 0, 7)
