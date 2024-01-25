import unittest
from task1_4 import solve

class TaskTest(unittest.TestCase):
    def test_test(self):
        self.assertEqual(solve(1,0,0), 0)
        self.assertEqual(solve(1,2,3), 7)
        self.assertEqual(solve(1,2,-3), "NO SOLUTION")
        self.assertEqual(solve(0,4,2), "MANY SOLUTIONS")
        self.assertEqual(solve(0,2,2), "NO SOLUTION")
        self.assertEqual(solve(2,5,0), "NO SOLUTION")