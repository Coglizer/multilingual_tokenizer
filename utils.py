### utils.py

from aramaic_dict import AramaicDictionary
from hebrew_dict import HebrewDictionary
from greek_dict import GreekDictionary
from latin_dict import LatinDictionary
from german_dict import GermanDictionary
from english_dict import EnglishDictionary


def get_ordered_dicts(paths):
    """
    Given a dict of language→folder, returns instances in this order:
    Aramaic, Hebrew, Greek, Latin, German, English.

    `paths` keys must match lower-case language names.
    """
    mapping = {
        'aramaic': AramaicDictionary,
        'hebrew': HebrewDictionary,
        'greek': GreekDictionary,
        'latin': LatinDictionary,
        'german': GermanDictionary,
        'english': EnglishDictionary,
    }
    order = ['aramaic', 'hebrew', 'greek', 'latin', 'german', 'english']
    return [mapping[lang](paths[lang]) for lang in order if lang in paths]
