''' Test translator functions '''

import unittest
from translator import french_to_english, english_to_french

class TestEnglishToFrench(unittest.TestCase):
    ''' Test english to french function '''
    def test1(self):
        ''' Test e2f for null and hello '''
        self.assertIsNone(english_to_french(''))
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    ''' Test french to english function '''
    def test1(self):
        ''' Test f2e for null and bonjour'''
        self.assertIsNone(french_to_english(''))
        self.assertEqual(french_to_english('Bonjour'),'Hello')
