import unittest

from Circle import Circle
from Triangle import Triangle


class Test_check_figure(unittest.TestCase):

    def test_get_length_triangle(self):
        triangle = Triangle(5, 6, 7)
        self.assertEqual(triangle.get_length(), 18.00)

    def test_get_square_triangle(self):
        triangle = Triangle(5, 6, 7)
        self.assertEqual(triangle.get_square(), 14.696938456699069)

    def test_get_length_circle(self):
        circle = Circle(5)
        self.assertEqual(circle.get_length(), 31.41592653589793)

    def test_get_square_circle(self):
        circle = Circle(5)
        self.assertEqual(circle.get_square(), 78.53981633974483)

    def test_check_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.check_right_triangle(), 'Треугольник со сторонами 3, 4, 5 прямоугольный')


if __name__ == '__main__':
    unittest.main(verbosity=2)