from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

"""renpy
init python:
"""


@dataclass
class TrackerData:
    data: ClassVar[list[TrackerData]] = []

    character: "NonPlayableCharacter"
    condition: bool
    true_text: str = ""
    false_text: str = ""

    def __post_init__(self) -> None:
        TrackerData.data.append(self)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, TrackerData):
            return NotImplemented

        return (
            self.character == __value.character
            and self.condition == __value.condition
            and self.true_text == __value.true_text
            and self.false_text == __value.false_text
        )
