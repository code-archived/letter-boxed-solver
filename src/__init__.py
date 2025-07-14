# -*- encoding: utf-8 -*-

"""
Source Code to Solve the New York Times Letter Boxed Puzzle

A Python Package to Solve the New York Times Letter Boxed Puzzle and
intutively understand the problem. To understand the working principle
check the readme file and example directory.

@author: Debmalya Pramanik
@copywright: 2024; Debmalya Pramanik (ZenithClown)
"""

# ? package follows https://peps.python.org/pep-0440/
# ? https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html
__version__ = "v0.0.1.dev0"

# init-time options registrations
from src.corpus import WordCorpus
from src.abstract import LetterBoxes
from src.model import LetterBoxedModel
