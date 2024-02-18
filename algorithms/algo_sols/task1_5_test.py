import unittest
from task1_5 import sol

class Test(unittest.TestCase):
    def test(self):
        cases = {
            (89, 20, 41, 1, 11) : (2, 3),

            # the known flat on the first cell 
            # but there's only one floor so it's safe 
            # you can go ahead and
            (11, 1, 1, 1, 1) : (0, 1), 

            # the known flat in the second entrance
            # of a one-storey building
            (11, 1, 3, 2, 1) : (6, 1),

            (3, 2, 2, 2, 1) : (-1, -1),
            (11, 2, 1, 1, 1) : (0, 0),
            (3, 3, 5, 1, 1) : (1, 1),
            (15, 10, 31, 4, 20) : (-1, -1),

            # N2>M flat is higher than maximum floor
            (11, 1, 5, 1, 2) : (-1, -1),
            # G_min > G_max
            (13, 2, 6, 2, 2) : (-1, -1)
        }

        for k, c in cases.items():
            self.assertEqual(sol(*k), c, msg=str(k))
