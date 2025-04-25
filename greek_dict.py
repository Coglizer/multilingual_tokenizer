
from base_dict import BaseDictionary
import unicodedata

class GreekDictionary(BaseDictionary):
    """Strips Greek diacritics (removes combining marks)."""
    def clean_word(self, word):
        nfkd = unicodedata.normalize('NFKD', word)
        return ''.join(c for c in nfkd if not unicodedata.category(c).startswith('M')).lower()
