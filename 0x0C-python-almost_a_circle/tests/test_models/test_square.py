import unittest
import io
import os
from contextlib import redirect_stdout
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class Test_Square(unittest.TestCase):

    def test_documentation(self):
        """ testing for the code on documentation """
        self.assertTrue(len(Square.__doc__) >= 20, "Short doc string")
        self.assertTrue(len(Square.display.__doc__) >= 20, "Short doc string")
        self.assertTrue(len(Square.update.__doc__) >= 20, "Short doc string")
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ testing pycodestyle for the square class """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/square.py',
                                     'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found no code style errors (and warnings).")

    def test_id(self):
        b = Square(2)
        self.assertEqual(b.id, 1)

    def test_unique_id(self):
        b = Square(4, 3, 3, 4)
        self.assertEqual(b.id, 4)

    def test_update(self):
        s = Square(2, 2, 2, 2)
        self.assertEqual("[Square] (2) 2/2 - 2", str(s))

    def test_kwargs(self):
        b = Square(2, 2, 2, 2)
        b.update(size=1, id=2)
        self.assertEqual("[Square] (2) 2/2 - 1", str(b))


if __name__ == "__main__":
    unittest.main()
