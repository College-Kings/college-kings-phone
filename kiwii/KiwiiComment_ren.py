"""renpy
init python:
"""

from __future__ import annotations
from dataclasses import dataclass, field
import random
from typing import Optional

from game.characters.ICharacter_ren import ICharacter
from game.phone.kiwii.KiwiiReply_ren import KiwiiReply


@dataclass
class KiwiiComment:
    user: ICharacter
    message: str
    number_likes: int = random.randint(250, 500)
    mentions: list[ICharacter] = field(default_factory=list)
    liked: bool = False
    replies: list[KiwiiReply] = field(default_factory=list)
    reply: Optional[KiwiiReply] = None
