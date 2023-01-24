''' Test translator functions '''

import unittest
from translator import frenchToEnglish, englishToFrench

class TestEnglishToFrench(unittest.TestCase):
    ''' Test english to french function '''
    def test1(self):
        ''' Test e2f for null and hello '''
        self.assertIsNone(englishToFrench(''))
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    ''' Test french to english function '''
    def test1(self):
        ''' Test f2e for null and bonjour'''
        self.assertIsNone(frenchToEnglish(''))
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
