import unittest

class UpDownTests(unittest.TestCase):

    def setUp(self):
        print("setUp run")

    def tearDown(self):
        print("tearDown run", end = "\n\n\n")

    def test_1(self):
        print("test_1 run")

    def test_2(self):
        print("test_2 run")
