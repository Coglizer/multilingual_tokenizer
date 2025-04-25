### base_dict.py

import os
import json

class BaseDictionary:
    """
    Base class for language dictionaries. Handles loading .txt files from a folder
    and assigning incremental IDs to each unique word.
    """
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.word_to_id = {}
        self.next_id = 1  # Start numbering from 1

    def load_files(self):
        """
        Reads all .txt files in the folder and returns a list of cleaned words.
        """
        words = []
        for fname in os.listdir(self.folder_path):
            if fname.endswith('.txt'):
                with open(os.path.join(self.folder_path, fname), 'r', encoding='utf-8') as f:
                    for line in f:
                        for token in line.strip().split():
                            cleaned = self.clean_word(token)
                            if cleaned:
                                words.append(cleaned)
        return words

    def clean_word(self, word):
        """
        Placeholder: override in subclasses to normalize/strip diacritics.
        """
        return word.lower()

    def build_dictionary(self):
        """
        Builds the mapping of word to ID.
        """
        for w in self.load_files():
            if w not in self.word_to_id:
                self.word_to_id[w] = self.next_id
                self.next_id += 1
        return self.word_to_id

    def export_json(self, output_path):
        """
        Exports the dictionary to JSON.
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.word_to_id, f, ensure_ascii=False, indent=2)
