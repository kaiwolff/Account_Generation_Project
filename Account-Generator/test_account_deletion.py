# delete account I have created

import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails


# use mock  package to run tests
class PassTest(unittest.TestCase):
    checker = UserAccountDetails()

    def test_delete_account(self):
        self.assertTrue(self.checker.delete_user("test_username", "test_manager", "test_password"))
    #check if the database has been updated
    def test_check_deletion(self):
        self.assertFalse(self.checker.check_existence("username"))
    #check if the account no longer exists
