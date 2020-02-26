"""
Test file for Triangle.py
"""
import unittest
from triangle import triangles

class StoriesTest(unittest.TestCase):
    """Testing Triangle.py"""

    def test_01(self):
        """Valid Input"""
        self.assertEqual(triangles(4, 4, 5), ["Isosceles Triangle"])
        self.assertEqual(triangles(3, 4, 6), ["Scalene Triangle"])
        self.assertEqual(triangles(4, 4, 4), ["Equilateral Triangle", 'Isosceles Triangle'])
        self.assertEqual(triangles(3, 4, 5), ['Scalene Triangle', "Right Angle Triangle"])
        self.assertEqual(triangles(4, 4, "x"), "Enter a valid set of inputs")
        self.assertEqual(triangles(4, 4, 0), "Enter non-zero values")
        self.assertEqual(triangles(3.5, 4.89, 6.876), ["Scalene Triangle"])
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
