import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pycodestyle


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
        self.assertEqual(r.y, 2)

    def test_id(self):
        r = Rectangle(1, 2, 3, 3, 2)
        self.assertEqual(r.id, 2)

    def test_pycodestyle(self):
        """ testing pycodestyle """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/rectangle.py',
                                     'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_for_documentation(self):
        """ testing for documentation """
        self.assertTrue(len(Rectangle.__doc__) >= 20, "too short Short doc")
        self.assertTrue(len(Rectangle.area.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.display.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.update.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 20, "Short")
        self.assertTrue(len(Rectangle.to_json_string.__doc__) >= 20, "Short")

    def test_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update()
        self.assertEqual("[Rectangle] (2) 2/2 - 2/2", str(r))

    def test_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r1))

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("e", 3)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "e")

    def test_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)

    def test_value_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4)

    def test_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)

    def test_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)

    def test_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)

    def test_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "hi")

    def test_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -2)

    def test_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 3, "hi")

    def test_y_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 4, 3, -5)


if __name__ == "__main__":
    unittest.main()
