import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails


class PassTest(unittest.TestCase):

    checker = UserAccountDetails()
    def test_existence(self):
        self.assertTrue(self.checker.check_existence(self,"duplicate_username"))

    def test_added(self):
        #begin by creating a new test_user_details
        self.assertFalse(self.checker.check_existence(self,"test_username"))
        #Change
        self.checker.create_new_user("test_firstname","test_lastname","test_username","password")
        self.assertTrue(self.checker.check_existence(self,"test_username"))
