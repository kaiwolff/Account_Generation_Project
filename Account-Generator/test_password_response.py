# as a user, I want to be prompted that my password is weak or strong  

import pytest 
import unittest 
import random

from strength_checker import StrengthChecker 

class StrengthChecker(unittest.Testcase):

	checker = StrengthChecker()

	def test_check(self):
		self.assertEqual(self.checker.password_strength_prompt("password"), "This password is weak")
		self.assertEqual(self.checker.password_strength_prompt("s$Y9h70OXO)nXb7Y"), "This password is strong")
		self.assertEqual(self.checker.password_strength_prompt("Afshanapw", "Afshana", "Begum", "1997"), "This password is weak")
		self.assertEqual(self.checker.password_strength_prompt("s$Y9h70OXO)nXb7Y", "Afshana", "Begum", "1997"), "This password is strong")

	
