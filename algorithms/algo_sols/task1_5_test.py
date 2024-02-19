import unittest
from task1_5 import sol

class Test(unittest.TestCase):
    def test(self):
        cases = {
            # just basic case
            (89, 20, 41, 1, 11) : (2, 3),
            # the known flat on the first cell 
            # but there's only one floor so it's safe 
            # you can go ahead and
            (11, 1, 1, 1, 1) : (0, 1), 
            # the known flat in the second entrance
            # of a one-storey building
            (11, 1, 3, 2, 1) : (6, 1),
            # T2 > K2
            (3, 2, 2, 2, 1) : (-1, -1),
            # we can't define G because there can be any
            # number of flats befind any flat on the first
            # stairwell of the first staircase and K1>K2
            (11, 2, 1, 1, 1) : (0, 0),
            # we can't define G because there can be any
            # number of flats behind any flat on the first
            # staircase, but K1<K2 which guarantees that the second
            # apartment is on the first staircase
            (3, 3, 5, 1, 1) : (1, 1),
            # G_min < G_max
            (15, 10, 31, 4, 20) : (-1, -1),

            # the following group of cases checking
            # belongs to pattern when G_min > G_max
            
            # one solution
            (2, 3, 4, 1, 2) : (1, 1),
            # several cases for N
            (6, 3, 4, 1, 2) : (1, 0),
            # several cases for both
            (9, 3, 4, 1, 2) : (0, 0),
            # several cases for P
            (15, 3, 4, 1, 2) : (0, 2),

            # N2>M flat is higher than maximum floor
            (11, 1, 5, 1, 2) : (-1, -1),
            # G_min > G_max
            (13, 2, 6, 2, 2) : (-1, -1)
        }

        for k, c in cases.items():
            self.assertEqual(sol(*k), c, msg=str(k))
