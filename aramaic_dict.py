### aramaic_dict.py

from base_dict import BaseDictionary

class AramaicDictionary(BaseDictionary):
    """Handles Aramaic-specific cleaning (strip non-alphanumeric)."""
    def clean_word(self, word):
        return ''.join(ch for ch in word if ch.isalnum())
