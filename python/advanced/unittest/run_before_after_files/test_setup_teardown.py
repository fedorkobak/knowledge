import unittest

class UpDownTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setUp run")

    @classmethod
    def tearDownClass(self):
        print("tearDown run", end = "\n\n\n")

    def test_1(self):
        print("test_1 run")

    def test_2(self):
        print("test_2 run")
