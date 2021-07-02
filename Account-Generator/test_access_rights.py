import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails

class TestAccessRights(unittest.TestCase):

    checker = UserAccountDetails()

    def test_access(self):
        #change user name
        #check admin
        self.assertTrue(self.checker.check_admin("admin","admin")) # Fun Checkadmin takes user,pass from input User login Test admin account
        self.assertEqual(self.checker.change_to_manager("TestUser","admin", "admin"),"The account has been changed to admin status.") # changing the TestUser account into a admin should return 1 row edited
        self.assertEqual(self.checker.change_to_user("TestUser","admin", "admin"),"The account has been changed to user")
        self.assertEqual(self.checker.change_username("TestUser", "NewAdmin"), "{} has been changed to {}.".format("TestUser", "NewAdmin"))#takes the Username and chnages it to the new username
