#!/usr/bin/python3
"""
Square unittest module
"""
import unittest
from models.square import Square

def setUpModule():
    pass
def tearDownModule():
    pass

class TestSquare(unittest.TestCase):
    """
    Square unittest
    """
    @classmethod
    def setUpRec(cls):
        pass

    @classmethod
    def tearDownRec(cls):
        pass

    def setUp(self):
        """
        creates objects
        """
        self.t1 = Square(1)
        self.t2 = Square(2, 3, 4, "id")

    def tearDown(self):
        """
        deletes objects
        """
        del self.t1
        del self.t2

    def test_correct_args(self):
        """
        assertEqual tests
        """
        self.assertEqual(self.t1.width, 1)
        self.assertEqual(self.t1.x, 0)
        self.assertEqual(self.t1.y, 0)
        self.assertEqual(self.t1.id, 4)

        self.assertEqual(self.t2.width, 2)
        self.assertEqual(self.t2.x, 3)
        self.assertEqual(self.t2.y, 4)
        self.assertEqual(self.t2.id, "id")
        
    def test_wrong_args(self):
        """
        assertRaises tests
        """
        self.assertRaises(ValueError, Square, size=0)
        self.assertRaises(ValueError, Square, 1, x=-1)
        self.assertRaises(TypeError, Square, 1, 1, y="world")
