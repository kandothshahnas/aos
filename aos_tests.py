import unittest
import aos_methods as methods
import aos_locators as locators


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user():
        methods.setup()
        methods.create_new_account()
        methods.check_username_display()
        methods.logout()
        methods.login()
        methods.check_username_display()
        methods.logout()
        methods.validate_dash_board()
        methods.teardown()
