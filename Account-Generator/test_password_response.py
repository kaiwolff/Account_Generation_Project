import pytest
import unittest
import configparser
import string
import random

from user_account_details import UserAccountDetails

class ResponseTest(unittest.TestCase):

	checker = UserAccountDetails()

	def test_check(self):
		self.assertEqual(self.checker.create_new_user("test_username","test_firstname","test_lastname", "1997", "password"), "Your password is weak.") # testing for password
		self.assertEqual(self.checker.create_new_user("test_username","test_firstname","test_lastname", "1997", "s$Y9h70OXO)nXb7Y"), "You have been successfully added to the database system.") # testing for password
		self.assertEqual(self.checker.create_new_user( "Afshana", "Afshana", "Begum", "1997", "Afshanapw"), "This password is weak.") # test checks is user details are in password
		self.assertEqual(self.checker.create_new_user("Afshana_username","Afshana", "Begum", "1997", "s$Y9h70OXO)nXb7Y"), "You have been successfully added to the database system.") 
