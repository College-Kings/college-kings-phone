from dataclasses import dataclass, field
import random
from typing import Optional, Sequence

from game.characters.character_ren import Character
from game.phone.kiwii.KiwiiBuilder_ren import KiwiiBuilder


"""renpy
init python:
"""


@dataclass
class KiwiiReply:
    message: str
    number_likes: int = random.randint(250, 500)
    mentions: Sequence[Character] = field(default_factory=list)
    next_comment: Optional[KiwiiBuilder] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.message})"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, KiwiiReply):
            return NotImplemented

        return self.message == __value.message
