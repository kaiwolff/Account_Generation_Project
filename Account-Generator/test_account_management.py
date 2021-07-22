import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails


class PassTest(unittest.TestCase):

    checker = UserAccountDetails()
    
    def test_login(self):
        self.checker.create_new_user("test_user", "test_first", "test_last", "1990", "7$!5I6c2-F1r7m1S")
        self.assertTrue(self.checker.user_login("test_user", "7$!5I6c2-F1r7m1S"))
        self.checker.delete_user("test_user", "admin", "admin")
    def test_existence(self):
        self.assertTrue(self.checker.check_existence("admin"))




# craete_new_user may have some issues with permantly adding to database otherwise 100%
