import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails

class TestAccessRights(unittest.TestCase):

    def test_access(self):
        #change user name
        #check admin

        checker = UserAccountDetails()

        self.assertTrue(self.checker.check_admin("admin","admin")) # Fun Checkadmin takes user,pass from input User login Test admin account
        self.assertEqual(self.checker.change_access("TestUser"),1) # changing the TestUser account into a admin should return 1 row edited
        self.assertEqual(self.checker.change_username("TestUser", "NewAdmin"),1)#takes the Username and chnages it to the new username
