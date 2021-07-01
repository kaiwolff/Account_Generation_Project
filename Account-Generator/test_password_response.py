import pytest
import unittest
import configparser
import string
import random

from password_checks import UserPasswordDetails

class ResponseTest(unittest.TestCase):

	checker = UserPasswordDetails()

	def test_check(self):
		self.assertEqual(self.checker.check_policy("password"), "This password is weak")
		self.assertEqual(self.checker.check_policy("s$Y9h70OXO)nXb7Y"), "This password is strong")
		self.assertEqual(self.checker.check_policy("Afshanapw", "Afshana", "Begum", "1997"), "This password is weak")
		self.assertEqual(self.checker.check_policy("s$Y9h70OXO)nXb7Y", "Afshana", "Begum", "1997"), "This password is strong")
