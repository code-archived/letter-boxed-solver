# -*- encoding: utf-8 -*-

"""
Read the Word Corpus from a File
"""

import os

WORDS_CORPUS = open(os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "assets", "words.txt"
)), "r", encoding = "utf-8").read().splitlines()
