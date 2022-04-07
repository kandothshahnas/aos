import unittest
import aos_methods as methods
import aos_locators as locators


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setup()
        methods.create_new_account()
        methods.logOut()
        methods.logIn(locators.aos_username, locators.aos_password)
        methods.logOut()
        methods.teardown()