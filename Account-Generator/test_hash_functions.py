import pytest
import unittest
import configparser
import string
import random

from hashfunctions import HashFunctions

class PassTest(unittest.TestCase):

    checker = HashFunctions()

    def test_hash(self):
        self.assertTrue(self.checker.check_pass("test_username1", "s$Y9h70OXO)nXb7Y"))
        self.assertFalse(self.checker.check_pass("WrongUserName", "s$Y9h70OXO)nXb7Y"))
        self.assertFalse(self.checker.check_pass("test_username1", "WrongPasswordHere"))

    def test_salt(self):
        self.assertEqual(self.checker.get_user_salt("test_username1"), "Njc0NjY2NDA3eTA2djk0")
