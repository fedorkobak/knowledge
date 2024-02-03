import unittest
from assert_raises import my_division

class MyCase(unittest.TestCase):
    def test_sucessfull(self):
        '''
        Case where division by zero occurs.
        So testing for it will be successful.
        '''
        self.assertRaises(
            ValueError,
            my_division,
            10, 0
        )

    def test_error(self):
        '''
        Case where division by zero doesn't happen.
        So testing for it won't finish well.
        '''
        self.assertRaises(
            ValueError,
            my_division,
            10,2
        )
