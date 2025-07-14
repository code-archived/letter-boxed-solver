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
        self,
        filepath : str = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "assets", "words.txt"
        ))
    ) -> None:
        """
        Initialize the Word Corpus from a File

        The initialization consider the static file from the
        ``assets`` directory (in the project root) and returns a
        list of valid words. In addition, a utility function is
        provided to update the corpus file using the ``nltk``
        corpus.
        """

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


    def update(self, normalize : bool = True) -> bool:
        """
        Update the Word Corpus File using ``nltk.corpus`` Module

        The update method directly overwrites the file with the
        words from the ``nltk.corpus`` module.

        :type  normalize: bool
        :param normalize: Normalize the words by setting all uppercase
            for words, such that it is easier to search and form a
            word from the valid letters.
        """

        nltk.download("words", quiet = True)
        corpus = words.words() # nltk corpus, not the file

        if normalize:
            corpus = list(map(lambda x : x.upper(), corpus))

        with open(self.filepath, "w", encoding = "utf-8") as file:
            for word in TQ(corpus, desc = "Updating File"):
                file.write(f"{word}\n")

        return True
