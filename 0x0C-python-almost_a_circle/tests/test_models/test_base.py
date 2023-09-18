import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Instantation(unittest.TestCase):
    """
    test for classes
    """

    def test_base(self):
        b = Base()
        b1 = Base()
        self.assertEqual(b.id, b1.id - 1)

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



if __name__ == '__main__':
    unittest.main()
