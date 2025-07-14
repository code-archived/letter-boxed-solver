# -*- encoding: utf-8 -*-

"""
Abstract Base Class for the Letter Boxed Puzzle Solver
"""

from pydantic import BaseModel, field_validator

class LetterBoxes(BaseModel):
    """
    The Abstract Data Class for Letters
    """

    L : list[str]
    R : list[str]
    T : list[str]
    B : list[str]

    @field_validator('L', 'R', 'T', 'B')
    @classmethod
    def check_letters(cls, value : list[str]) -> list[str]:
        """
        Validate the Letters in Each Box
        """

        assert len(value) == 3, "Each box must contain exactly 3 letters."
        assert len(set(value)) == 3, "Each box must contain 3 unique letters."

        return value


    @property
    def letters(self) -> list[str]:
        return self.L + self.R + self.T + self.B


    @property
    def sides(self) -> dict[str, list[str]]:
        """
        Return a Dictionary of Valid Sides

        The keys are returned as a string, and can be used for
        comparison and finding the side for a given letter.
        """

        return {
            "L" : self.L,
            "R" : self.R,
            "T" : self.T,
            "B" : self.B
        }


    def getside(self, char : str) -> str:
        """
        Return the Side Name (letter) for a Given Letter

        The side name to which the letter belongs is returned as a
        string, and can be used for comparison and tossing a word.
        """

        return next(
            (
                key for key, valid in self.sides.items()
                if char in valid # type: ignore, current char is valid
            ),
            None
        )


    def nlvalid(self, char : str, nchar : str) -> bool:
        """
        Check if the Next Letter is Valid

        Given a letter (``char``) and the next letter (``nchar``) the
        function checks if the next letter is valid. The NY solver
        cannot be formed if two letters are in the same leg.
        """

        return self.getside(char) != self.getside(nchar)
