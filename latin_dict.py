### latin_dict.py

from base_dict import BaseDictionary
import unicodedata

class LatinDictionary(BaseDictionary):
    """Strips Latin diacritics (removes combining marks)."""
    def clean_word(self, word):
        nfkd = unicodedata.normalize('NFKD', word)
        return ''.join(c for c in nfkd if not unicodedata.category(c).startswith('M')).lower()
