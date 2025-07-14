# -*- encoding: utf-8 -*-

"""
Scrape New York Times Letter Boxed Puzzle

Webscrape to get the letters for today's NY Times Letter Boxed Puzzle
automatically, can be used to get the solution to the puzzle.
"""

import json
import requests

from bs4 import BeautifulSoup

from src.abstract import LetterBoxes

class ScrapeLetterBox:
    def __init__(
        self,
        uri : str = "https://www.nytimes.com/puzzles/letter-boxed"
    ) -> None:
        self.uri = uri
        self.data = self.getdata(
            tag = "script",
            obj = "window.gameData"
        )

    @property
    def response(self) -> requests.Response:
        return requests.get(self.uri).text


    def getdata(self, tag : str, obj : str) -> dict:
        soups = BeautifulSoup(self.response, "html.parser")
        script = [
            script.text for script in soups.find_all(tag)
            if script.text.startswith(obj)
        ][0]

        return json.loads(
            f"""{script}""".replace("window.gameData = ", "")
        )


    @property
    def sides(self) -> LetterBoxes:
        return LetterBoxes(
            T = list(self.data["sides"][0]),
            R = list(self.data["sides"][1]),
            B = list(self.data["sides"][2]),
            L = list(self.data["sides"][3])
        )


    @property
    def corpus(self) -> list[str]:
        return self.data["dictionary"]


    def nysolution(self) -> list[str]:
        return self.data["ourSolution"]
