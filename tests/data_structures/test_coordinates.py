from math import sqrt

from data_structures import Coordinates


class TestCoordinates:
    def test_initialization(self):
        coordinates = Coordinates(x=1, y=2, z=3, w=4)

        assert coordinates.x == 1
        assert coordinates.y == 2
        assert coordinates.z == 3
        assert coordinates.w == 4

    def test_is_point(self):
        coordinates = Coordinates(x=0, y=0, z=0, w=1)

        assert coordinates.is_point()
        assert not coordinates.is_vector()

    def test_is_vector(self):
        coordinates = Coordinates(x=0, y=0, z=0, w=0)

        assert not coordinates.is_point()
        assert coordinates.is_vector()

    def test_point_conveniece_constructor(self):
        coordinates = Coordinates.point(1, 2, 3)

        assert coordinates.is_point()
        assert not coordinates.is_vector()

    def test_vector_conveniece_constructor(self):
        coordinates = Coordinates.vector(1, 2, 3)

        assert not coordinates.is_point()
        assert coordinates.is_vector()

    def test_coordinates_addition(self):
        coord_1 = Coordinates(x=3, y=-2, z=5, w=1)
        coord_2 = Coordinates(x=-2, y=3, z=1, w=0)

        result = coord_1 + coord_2

        assert result == Coordinates(x=1, y=1, z=6, w=1)

    def test_subtract_points(self):
        p1 = Coordinates.point(x=3, y=2, z=1)
        p2 = Coordinates.point(x=5, y=6, z=7)

        result = p1 - p2

        assert result == Coordinates.vector(x=-2, y=-4, z=-6)
        assert result.is_vector()

    def test_subtract_vector_from_point(self):
        point = Coordinates.point(3, 2, 1)
        vector = Coordinates.vector(5, 6, 7)

        result = point - vector

        assert result == Coordinates.point(-2, -4, -6)
        assert result.is_point()

    def test_subtract_vectors(self):
        v1 = Coordinates.vector(3, 2, 1)
        v2 = Coordinates.vector(5, 6, 7)

        result = v1 - v2

        assert result == Coordinates.vector(-2, -4, -6)
        assert result.is_vector()

    def test_subtracting_vector_from_zero(self):
        v1 = Coordinates.vector(0, 0, 0)
        v2 = Coordinates.vector(1, -2, 3)

        result = v1 - v2

        assert result == Coordinates.vector(-1, 2, -3)

    def test_negating_coordinates(self):
        coord = Coordinates(x=1, y=-2, z=3, w=-4)

        result = -coord

        assert result == Coordinates(x=-1, y=2, z=-3, w=4)

    def test_multiplying_coordinate_by_scalar(self):
        coord = Coordinates(1, -2, 3, -4)

        result = coord * 3.5

        assert result == Coordinates(3.5, -7.0, 10.5, -14.0)

    def test_multiplying_coordinates_by_fraction(self):
        coord = Coordinates(1, -2, 3, -4)

        result = coord * 0.5

        assert result == Coordinates(0.5, -1.0, 1.5, -2.0)

    def test_dividing_coordinates_by_scalar(self):
        coord = Coordinates(1, -2, 3, -4)

        result = coord / 2

        assert result == Coordinates(0.5, -1.0, 1.5, -2.0)

    def test_magnitude_of_vector_1_0_0(self):
        v = Coordinates.vector(1, 0, 0)
        result = v.magnitude()

        assert result == 1.0

    def test_magnitude_of_vector_0_1_0(self):
        v = Coordinates.vector(1, 0, 0)

        result = v.magnitude()

        assert result == 1.0

    def test_magnitude_of_vector_0_0_1(self):
        v = Coordinates.vector(1, 0, 0)

        result = v.magnitude()

        assert result == 1.0

    def test_magnitude_of_vector_1_2_3(self):
        v = Coordinates.vector(1, 2, 3)

        result = v.magnitude()

        assert result == sqrt(14)

    def test_normalize_vector_4_0_0(self):
        v = Coordinates.vector(4, 0, 0)

        result = v.normalize()

        assert result == Coordinates.vector(1, 0, 0)

    def test_normalize_vector_1_2_3(self):
        v = Coordinates.vector(1, 2, 3)

        result = v.normalize()

        assert round(result.x, 5) == 0.26726
        assert round(result.y, 5) == 0.53452
        assert round(result.z, 5) == 0.80178

    def test_magnitude_of_normalized_vector_is_1(self):
        v = Coordinates.vector(1, 2, 3)

        result = v.normalize().magnitude()

        assert result == 1.0

    def test_dot_product(self):
        v1 = Coordinates.vector(1, 2, 3)
        v2 = Coordinates.vector(2, 3, 4)

        result = v1.dot_product(v2)

        assert result == 20

    def test_cross_product(self):
        v1 = Coordinates.vector(1, 2, 3)
        v2 = Coordinates.vector(2, 3, 4)

        result1 = v1.cross_product(v2)
        result2 = v2.cross_product(v1)

        assert result1 == Coordinates.vector(-1, 2, -1)
        assert result2 == Coordinates.vector(1, -2, 1)
