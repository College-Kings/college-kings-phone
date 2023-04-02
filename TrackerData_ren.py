"""renpy
init python:
"""

from __future__ import annotations
from typing import TYPE_CHECKING, ClassVar
from dataclasses import dataclass

if TYPE_CHECKING:
    from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter


@dataclass
class TrackerData:
    data: ClassVar[list[TrackerData]] = []

    character: NonPlayableCharacter
    condition: bool
    true_text: str = ""
    false_text: str = ""

    def __post_init__(self) -> None:
        TrackerData.data.append(self)
