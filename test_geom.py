import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(circle.area(5), math.pi * 25)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0.0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-3)


if __name__ == "__main__":
    unittest.main()