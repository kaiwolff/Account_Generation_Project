# delete account I have created

import pytest
import unittest
import configparser
import string
import random

from Password_Analyzer import PasswordChecker

# use mock  package to run tests
class PassTest(unittest.TestCase):
        checker = AccountChecker()
        manage = AccountManager()
    def test_delete_account(self):
        self.assertTrue(self.table_update(self, "something"))
    #check if the database has been updat
    def test_check_deletion(self):
        self.assertFalse(self.check_existence(self, "username"))
    #check if the account no longer exists
