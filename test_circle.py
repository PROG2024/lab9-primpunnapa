"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle
import math


class CircleTest(unittest.TestCase):

    def test_typical_values(self):
        """test when typical values"""
        c1 = Circle(2)
        c2 = Circle(3)
        c3 = c1.add_area(c2)
        c3_area = math.pi * (c3.get_radius()**2)
        c3_radius = math.hypot(c1.get_radius(), c2.get_radius())
        self.assertEqual(c3.get_radius(), c3_radius)
        self.assertEqual(c3.get_area(), c3_area)

    def test_radius_is_zero(self):
        """test radius is zero"""
        c1 = Circle(5)
        c2 = Circle(0)
        c3 = c1.add_area(c2)
        c3_area = math.pi * (c3.get_radius()**2)
        self.assertEqual(c3.get_radius(), c1.get_radius())
        self.assertEqual(c3.get_area(), c3_area)

    def test_radius_cannot_be_negative(self):
        """test radius cannot be negative"""
        with self.assertRaises(ValueError):
            c2 = Circle(-1)
