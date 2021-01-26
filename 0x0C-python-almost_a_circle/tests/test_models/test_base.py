#!/usr/bin/python3
"""
Base unittest module
"""
import unittest
from models.base import Base

def setUpModule():
    pass
def tearDownModule():
    pass

class TestBase(unittest.TestCase):
    """
    Base unittests
    """
    @classmethod
    def setUpBase(cls):
        pass

    @classmethod
    def tearDownBase(cls):
        pass

    def setUp(self):
        """
        creates objects
        """
        self.t1 = Base()
        self.t2 = Base(0)
        self.t3 = Base(1)
        self.t4 = Base(-7)
        self.t5 = Base('a')
        self.t6 = Base(12.156)
        self.t7 = Base([0, 1, 2])
        self.t8 = Base((0, 1))
        self.t9 = Base("string")

    def tearDown(self):
        """
        deletes objects
        """
        del self.t1
        del self.t2
        del self.t3
        del self.t4
        del self.t5
        del self.t6
        del self.t7
        del self.t8
        del self.t9

    def test_id_cases(self):
        """
        assertEqual tests
        """
        self.assertEqual(self.t1.id, 1)
        self.assertEqual(self.t2.id, 0)
        self.assertEqual(self.t3.id, 1)
        self.assertEqual(self.t4.id, -7)
        self.assertEqual(self.t5.id, 'a')
        self.assertEqual(self.t6.id, 12.156)
        self.assertEqual(self.t7.id, [0, 1, 2])
        self.assertEqual(self.t8.id, (0, 1))
        self.assertEqual(self.t9.id, "string")
