# -*- encoding: utf-8 -*-

"""
Model for the Letter Boxed Puzzle Solver
"""

from collections import defaultdict
from src.abstract import LetterBoxes

class LetterBoxedModel:
    def __init__(self, boxes: LetterBoxes, words : list[str]) -> None:
        """
        Initialize the Letter Boxed Model
        """

        self.boxes = boxes
        self.words = sorted(self.__subset_words__(words))


    def __subset_words__(self, words : list[str]) -> list[str]:
        """
        Create a Subset of Words from the Word Corpus

        The subset of words is created by filtering the words from
        the corpus, based on the letters in the boxes.

        :type  words: list[str]
        :param words: List of words from the Word Corpus, typically
            from the ``nltk.corpus.words`` module.
        """

        chars = set(self.boxes.letters)

        return [
            word for word in words
            if set(word).issubset(set(chars)) and self.toss(word)
        ]


    def toss(self, word : str) -> bool:
        """
        Toss a Word and Check if it is Valid based on the Boxes

        The word tossing is an extensive search that compares each
        letter of the word and validates if the next element is a
        valid letter, based on the current letter.

        :type  word: str
        :param word: Word to be tossed, check if all the adjacent
            letters are not from the same boxes side of the box.
        """

        return all([
            self.boxes.nlvalid(left, right)
            for left, right in zip(word[:-1], word[1:])
        ])


    @property
    def indexed(self) -> dict[str, list[str]]:
        """
        Return a Pre-Index Dictionary of Words by the First Letter
        """

        indexed = defaultdict(list)

        for word in self.words:
            indexed[word[0]].append(word)

        return indexed


    def solve(self, nwords : int) -> list[str]:
        """
        NY Letter Boxed Solution using Backtracking

        The model finds solutions for the NY Letter Boxed Puzzle
        using backtracking, and returns a list of words that are
        valid solutions.

        :type  nwords: int
        :param nwords: Number of words to be found using which the
            solution is to be calculated.
        """

        return {
            # ? one word solution, set must be same as all words valid
            1 : [
                word for word in self.words
                if set(self.boxes.letters) - set(word) == set()
            ],
        }.get(nwords, [])
