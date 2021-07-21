import pytest
import unittest

from hashfunctions import HashFunctions
from user_account_details import UserAccountDetails

class PassTest(unittest.TestCase):

    checker = HashFunctions()
    UserDetails = UserAccountDetails()

    def test_hash(self):
        self.UserDetails.create_new_user("test_username1", "test_first", "test_last", "1990", "sOXO)nXb7Y")
        self.assertTrue(self.checker.check_pass("test_username1", "sOXO)nXb7Y"))
        self.assertFalse(self.checker.check_pass("WrongUserName", "sOXO)nXb7Y"))
        self.assertFalse(self.checker.check_pass("test_username1", "WrongPasswordHere"))

    def test_salt(self):
        self.assertTrue(self.checker.get_user_salt("test_username1"))
        self.UserDetails.delete_user("test_username1", "admin", "admin")
