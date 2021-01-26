#!/usr/bin/python3
"""
Rectangle unittest module
"""
import unittest
from models.rectangle import Rectangle

def setUpModule():
    pass
def tearDownModule():
    pass

class TestRectangle(unittest.TestCase):
    """
    Rectangle unittest
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
        self.t1 = Rectangle(1, 2)
        self.t2 = Rectangle(3, 4, 5, 6, "id")

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
        self.assertEqual(self.t1.height, 2)
        self.assertEqual(self.t1.x, 0)
        self.assertEqual(self.t1.y, 0)
        self.assertEqual(self.t1.id, 2)

        self.assertEqual(self.t2.width, 3)
        self.assertEqual(self.t2.height, 4)
        self.assertEqual(self.t2.x, 5)
        self.assertEqual(self.t2.y, 6)
        self.assertEqual(self.t2.id, "id")
        
    def test_wrong_args(self):
        """
        assertRaises tests
        """
        self.assertRaises(ValueError, Rectangle, 1, height=0)
        self.assertRaises(TypeError, Rectangle, 1, height="hello")
        self.assertRaises(ValueError, Rectangle, 1, 1, x=-1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, y="world")
