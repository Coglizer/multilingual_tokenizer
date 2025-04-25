### german_dict.py

from base_dict import BaseDictionary

class GermanDictionary(BaseDictionary):
    """Normalizes German umlauts and ß (e.g. ä→ae, ß→ss)."""
    def clean_word(self, word):
        replacements = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'Ä': 'AE', 'Ö': 'OE', 'Ü': 'UE', 'ß': 'ss'}
        for src, tgt in replacements.items():
            word = word.replace(src, tgt)
        return ''.join(ch for ch in word if ch.isalnum()).lower()

