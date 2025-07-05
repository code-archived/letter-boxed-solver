# -*- encoding: utf-8 -*-

"""
Read the Word Corpus from a File
"""

import os
import nltk

from tqdm import tqdm as TQ
from nltk.corpus import words

class WordCorpus:
    def __init__(
        self, filepath : str = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "assets", "words.txt"
        ))
    ) -> None:
        self.filepath = filepath


    @property
    def words(self) -> list[str]:
        """
        Read the Word Corpus from the File

        The file lists all the words in the corpus, but for the
        solver, we only filter the required words which are valid:
        (i) length must be greater than 3, and (ii) the words must
        contain only unique letters.
        """

        with open(self.filepath, "r", encoding = "utf-8") as file:
            words = file.read().splitlines()

        return [
            word for word in words
            if (len(word) > 3) and len(set(word)) == len(word)
        ]


    def update(self, normalize : bool = True) -> None:
        nltk.download("words", quiet = True)
        corpus = words.words() # nltk corpus, not the file

        if normalize:
            corpus = list(map(lambda x : x.upper(), corpus))

        with open(self.filepath, "w", encoding = "utf-8") as file:
            for word in TQ(corpus, desc = "Updating File"):
                file.write(f"{word}\n")

        return True
