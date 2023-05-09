from __future__ import annotations
from dataclasses import dataclass, field
import random
from typing import Optional

from game.characters.ICharacter_ren import ICharacter
from game.phone.kiwii.KiwiiBuilder_ren import KiwiiBuilder


"""renpy
init python:
"""


@dataclass
class KiwiiReply:
    message: str
    number_likes: int = random.randint(250, 500)
    mentions: list[ICharacter] = field(default_factory=list)
    next_comment: Optional[KiwiiBuilder] = None
