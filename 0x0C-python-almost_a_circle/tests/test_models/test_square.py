import unittest
from io import StringIO
from unittest.mock import patch
import os
from contextlib import redirect_stdout
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class Test_Square(unittest.TestCase):
    """
    Testing classs for square
    """
    def setUp(self):
        """ a setup setup method """
        Base._Base__nb_objects = 0
        self.s1 = Square(10, 5, 2, 11)
        self.s2 = Square(4, 4, 1)
        self.s3 = Square(3, 2, 2)

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
        b = Square(2, 3, 4, 3)
        self.assertEqual(b.id, 3)

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

    def test_diplay(self):
        with patch('sys.stdout', new_callable=StringIO) as std:
            Square(2).display()
        self.assertEqual("##\n##\n", std.getvalue())

    def test_area(self):
        self.assertEqual(Square(2).area(), 4)


if __name__ == "__main__":
    unittest.main()
