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
