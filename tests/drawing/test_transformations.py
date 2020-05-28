from data_structures import Coordinates
from drawing.transformations import translation


class TestTranslation:
    def test_multiplying_translation_matrix(self):
        transform = translation(5, -3, 2)
        point = Coordinates.point(-3, 4, 5)

        result = tranform * point

        assert result == Coordinates.point(2, 1, 7)

    def test_multiplying_by_inverse_of_translation_matrix(self):
        transform = translation(5, -3, 2)
        inverse = transform.inverse()
        point = Coordinates.point(-3, 4, 5)

        result = inverse * point

        assert result == Coordinates.point(-8, 7, 3)
