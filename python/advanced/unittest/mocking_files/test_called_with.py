import unittest
from unittest.mock import patch
from called_with import sum_wrapper

class TestCalledWiht(unittest.TestCase):
    def test_sum_wrapper1(self):
        with patch("called_with.sum") as mocked_sum:
            sum_wrapper([1,2,3])
            mocked_sum.assert_called_with([1,2,3])

    def test_sub_wrapper2(self):
        with patch("called_with.sum") as mocked_sum:
            sum_wrapper([1,2,5])
            mocked_sum.assert_called_with([1,2,3])            
