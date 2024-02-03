import unittest
from assert_raises import my_division

class MyCase(unittest.TestCase):
    def test_case(self):
        with self.assertRaises(ValueError):
            my_division(10, 0)
