import pytest
import unittest
import configparser
import string
import random

from password_checks import UserPasswordDetails


class HashTest(unittest.TestCase):

    checker = UserAccountDetails()
    def test_password_hash():
        self.assertEquals(self.checker.hashpass("helloworld","jamesdidit72") "d49cfc7c98a3cca0d60d80174a38c2b96e0fcdd3e4f44e702448f858aef63c9d")
