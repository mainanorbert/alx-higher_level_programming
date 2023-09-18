import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pycodestyle


class Test_Instantation(unittest.TestCase):
    """
    test for classes
    """

    def test_base(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_unique_id(self):
        b = Base(30)
        self.assertEqual(b.id, 30)

    def test_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_str(self):
        self.assertEqual("hi", Base("hi").id)

    def test_bytes(self):
        self.assertEqual(b'hi', Base(b'hi').id)

    def test_documentation(self):
        """ tests for documentation """
        self.assertTrue(len(Base.__doc__) >= 20, "Short or no documentation")
        self.assertTrue(len(Base.to_json_string.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.save_to_file.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.from_json_string.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.create.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.load_from_file.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ tests for pycodestyle """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/base.py',
                                     'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
