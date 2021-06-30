import pytest
import unittest
import configparser
import string
import random

from Password_Analyzer import AccountChecker, PasswordChecker


class WeakUser(unittest.TestCase):

    pwd_strength = AccountChecker()

    def test_existence(self):
        self.assertTrue(self.check_existence(self, "duplicate_username"))

    def test_password(self):
        self.pwd_strength.create_new_user("first_name","last_name","username","password")

        checker = PasswordChecker()

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
            self.assertEqual(self.checker.read_password_policy(),[1, 3, 3, 4, 8, 16, "~!$^&*()_-+="])
