import unittest
from solution import sol, potential_transformation

class Test(unittest.TestCase):
    def test_sol(self):
        '''
        Testing main function of the solution
        '''
        cases = [
            # just basic case
            ({'K1': 89, 'M': 20, 'K2': 41, 'P2': 1, 'N2': 11}, (2, 3)),
            # the known flat on the first cell 
            # but there's only one floor so it's safe 
            # you can go ahead and
            ({'K1': 11, 'M': 1, 'K2': 1, 'P2': 1, 'N2': 1}, (0, 1)), 
            # the known flat in the second entrance
            # of a one-storey building
            ({'K1': 11, 'M': 1, 'K2': 3, 'P2': 2, 'N2': 1}, (6, 1)),
            # T2 > K2
            ({'K1': 3, 'M': 2, 'K2': 2, 'P2': 2, 'N2': 1}, (-1, -1)),
            # we can't define G because there can be any
            # number of flats befind any flat on the first
            # stairwell of the first staircase and K1>K2
            ({'K1': 11, 'M': 2, 'K2': 1, 'P2': 1, 'N2': 1}, (0, 0)),
            # we can't define G because there can be any
            # number of flats behind any flat on the first
            # staircase, but K1<K2 which guarantees that the second
            # apartment is on the first staircase
            ({'K1': 3, 'M': 3, 'K2': 5, 'P2': 1, 'N2': 1}, (1, 1)),
            # we can't define G and number of stairswells, but number
            # of the dwelling in question is not large enough
            # to be in the next staircase
            ({'K1': 10, 'M': 3, 'K2': 5, 'P2': 1, 'N2': 1}, (1, 0)),
            # G_min < G_max
            ({'K1': 15, 'M': 10, 'K2': 31, 'P2': 4, 'N2': 20}, (-1, -1)),

            # the following group of cases checking
            # belongs to pattern when G_min > G_max
            
            # one solution
            ({'K1': 2, 'M': 3, 'K2': 4, 'P2': 1, 'N2': 2}, (1, 1)),
            # several cases for N
            ({'K1': 6, 'M': 3, 'K2': 4, 'P2': 1, 'N2': 2}, (1, 0)),
            # this is specific subcase for several N
            # there is G_max - G_min = 3 so there are
            # several iterations of the solution-finding loop
            ({'K1': 14, 'M': 3, 'K2': 18, 'P2': 1, 'N2': 3}, (1, 0)),
            # several cases for both
            ({'K1': 9, 'M': 3, 'K2': 4, 'P2': 1, 'N2': 2}, (0, 0)),
            # several cases for P
            ({'K1': 15, 'M': 3, 'K2': 4, 'P2': 1, 'N2': 2}, (0, 2)),

            # N2>M flat is higher than maximum floor
            ({'K1': 11, 'M': 1, 'K2': 5, 'P2': 1, 'N2': 2}, (-1, -1)),
            # G_min > G_max
            ({'K1': 13, 'M': 2, 'K2': 6, 'P2': 2, 'N2': 2}, (-1, -1))
        ]

        for k, c in cases:
            self.assertEqual(sol(**k), c, msg=str(k))

    def test_potential_transformation(self):
        '''
        Tests for funtion `potential_transformation`.
        I caught a bug in this function.
        '''
        cases = [
            # a case where ambiguity of judgement 
            # has already been established
            # and funtion have to return zero again
            ({"curr":0, "pot": 10}, 0),
            # if we trying to replace curr with
            # the same value we have ot leave same value
            ({"curr":10, "pot":10}, 10),
            # if curr isn't defined yet we have
            # to set it with potential value
            ({"curr":None, "pot":10}, 10),
            # if curr was set and we found
            # another potential value - return
            # marker of ambiguity
            ({"curr":10, "pot":9}, 0)
        ]

        for arg, ret in cases:
            self.assertEqual(potential_transformation(**arg), ret, msg=str(arg))
