from __future__ import annotations
from dataclasses import dataclass, field
import random
from typing import Optional, TYPE_CHECKING

from game.characters.ICharacter_ren import ICharacter

if TYPE_CHECKING:
    from game.phone.kiwii.KiwiiReply_ren import KiwiiReply

"""renpy
init python:
"""


@dataclass
class KiwiiComment:
    user: ICharacter
    message: str
    number_likes: int = random.randint(250, 500)
    mentions: list[ICharacter] = field(default_factory=list)
    liked: bool = False
    replies: list[KiwiiReply] = field(default_factory=list)
    reply: Optional[KiwiiReply] = None
