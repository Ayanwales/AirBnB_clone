#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.user import User


class Testuser(unittest.TestCase):
    """ TesteUser """
    def test_pep8_conformance_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")


class TestUser(unittest.TestCase):
    """ unit test for class user"""
    def test_User(self):
        """
            Test attributes of Class Use
        """
        my_user = User()
        my_user.first_name = 'Ayanwale'
        my_user.last_name = 'Sulaimon'
        my_user.email = 'ayanwalesulaymon@gmail.com'
        self.assertEqual(my_user.first_name, 'Ayanwale')
        self.assertEqual(my_user.last_name, 'Sulaimon')
        self.assertEqual(my_user.email, 'ayanwalesulaymon@gmail.com')
