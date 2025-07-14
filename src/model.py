# -*- encoding: utf-8 -*-

"""
Model for the Letter Boxed Puzzle Solver
"""

from src.abstract import LetterBoxes

class LetterBoxedModel:
    def __init__(self, boxes: LetterBoxes, words : list[str]) -> None:
        """
        Initialize the Letter Boxed Model
        """

        self.boxes = boxes
        self.words = self.__subset_words__(words)


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
