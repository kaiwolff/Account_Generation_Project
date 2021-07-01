import pytest
import unittest
import configparser
import string
import random

from  password_checks import UserPasswordDetails


class PassTest(unittest.TestCase):

    checker = UserPasswordDetails()

    def test_policy(self):
        self.assertFalse(self.checker.check_policy("password"))
        self.assertTrue(self.checker.check_policy("s$Y9h70OXO)nXb7Y"))

    def test_list(self):
        self.assertFalse(self.checker.check_list("password"))
        self.assertTrue(self.checker.check_list("s$Y9h70OXO)nXb7Y"))

    def test_user_details(self):
        self.assertFalse(self.checker.check_user_details("passwordKai","Kai", "Wolff","1992"))
        self.assertFalse(self.checker.check_user_details("passwordWolff", "Kai", "Wolff", "1992"))
        self.assertFalse(self.checker.check_user_details("password1992", "Kai", "Wolff", "1992"))
        self.assertTrue(self.checker.check_user_details("s$Y9h70OXO)nXb7Y", "Kai", "Wolff", "1992"))

    def test_read_policy(self):
        self.assertEqual(self.checker.read_password_policy(),[1, 3, 3, 4, 8, 16, "~!$^*()_-+="])
