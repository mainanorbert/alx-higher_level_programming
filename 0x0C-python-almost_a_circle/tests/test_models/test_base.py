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
        """ testing for for documentation """
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

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(
            [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]),
                '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_empty_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 5)])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(
            '[{"height": 4, "width": 10, "id": 89}]'),
            [{'height': 4, 'width': 10, 'id': 89}])

    def test_create(self):
        x = Rectangle(3, 5, 1, 2, 7)
        y = x.to_dictionary()
        x1 = Rectangle.create(**y)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(x1))

    def test_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        my_list = [r1]
        Rectangle.save_to_file_csv(my_list)
        list_out = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_out[0]))


if __name__ == '__main__':
    unittest.main()
