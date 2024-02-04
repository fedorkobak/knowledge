import unittest
from unittest.mock import patch
from request_user import request_user

class TestUserReques(unittest.TestCase):
    
    def test_success_case(self):
        with patch("request_user.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            
            response = request_user("Fedor")
            mocked_get.assert_called_with("https://im_not_exist/Fedor")
            self.assertEqual(response, "Success")

    def test_fail_case(self):
        with patch("request_user.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "Success"
            
            response = request_user("Ekaterina")
            mocked_get.assert_called_with("https://im_not_exist/Ekaterina")
            self.assertEqual(response, "Fail!")
