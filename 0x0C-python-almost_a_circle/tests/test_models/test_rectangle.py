import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rect(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_width_getter(self):
        r = Rectangle(3, 4, 4)
        self.assertEqual(r.width, 3)

    def test_width_getter(self):
        r = Rectangle(6, 4, 3, 23)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_height_getter(self):
        r = Rectangle(3, 4, 5, 3, 4)
        self.assertEqual(r.height, 4)

    def test_x_getter(self):
        r = Rectangle(4, 3, 3)
        self.assertEqual(r.x, 3)

    def test_y_getter(self):
        r = Rectangle(3, 4, 3, 2)
        self.assertEqual(r.y, 22)
