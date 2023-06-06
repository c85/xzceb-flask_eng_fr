import unittest
from tests import english_to_french, french_to_english

class TestEnglishTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when word is ‘Hello’ then ‘Bonjour’
        
class TestFrenchTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when word is ‘Bonjour’ then ‘Hello’
        
unittest.main()