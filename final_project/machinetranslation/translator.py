"""Module containing English-French and French-English translation functions."""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Function translates English to French."""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Function translates French to English."""
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
