import unittest

class SomeTest(unittest.TestCase):
    def test(self):
        print("simple test")
        self.assertEqual(10,10)
