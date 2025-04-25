### english_dict.py

from base_dict import BaseDictionary
import string

class EnglishDictionary(BaseDictionary):
    """Basic cleaning for English: strips leading/trailing punctuation."""
    def clean_word(self, word):
        return word.strip(string.punctuation).lower()
