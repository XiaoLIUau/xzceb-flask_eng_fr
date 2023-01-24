import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url('{url}')

'''Function english to french'''
def englishToFrench(englishText):
    '''Function take english text and translate to french'''
    translation = language_translator.translate(
    text = englishText,
    model_id = 'en-fr').get_result()
    frenchText = translation.get('translations')[0].get('translation')
    return frenchText

'''Function french to english'''
def frenchToEnglish(frenchText):
    '''Function take french text and translate to english'''
    translation = language_translator.translate(
    text = frenchText,
    model_id = 'fr-en').get_result()
    englishText = translation.get('translations')[0].get('translation')
    return englishText
