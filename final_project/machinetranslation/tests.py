''' Test translator functions '''

import unittest
# from translator import french_to_english, english_to_french
import translator

class TestEnglishToFrench(unittest.TestCase):
    ''' Test english to french function '''
    def test1(self):
        ''' Test e2f for null and hello '''
        # Test None input
        noneInput = None
        notNoneMag = 'Input is not none'
        self.assertIsNone(noneInput,notNoneMag)

        # Test not none input
        inputText = 'Hello'
        noneMsg = 'Input is none'
        self.assertIsNotNone(translator.english_to_french(inputText),noneMsg)
        self.assertEqual(translator.english_to_french(inputText),'Bonjour')
        self.assertNotEqual(translator.english_to_french(inputText),'bonsoir')

class TestFrenchToEnglish(unittest.TestCase):
    ''' Test french to english function '''
    def test1(self):
        ''' Test f2e for null and bonjour'''
        # Test None input
        noneInput = None
        notNoneMag = 'Input is not none'
        self.assertIsNone(noneInput,notNoneMag)

        # Test not none input
        inputText = 'Bonjour'
        noneMsg = 'Input is none'
        self.assertIsNotNone(translator.french_to_english(inputText),noneMsg)
        self.assertEqual(translator.french_to_english(inputText),'Hello')
        self.assertNotEqual(translator.french_to_english(inputText),'good evening')

if __name__ == "__main__":
    unittest.main()