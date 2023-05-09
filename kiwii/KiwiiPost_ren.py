from __future__ import annotations
from dataclasses import dataclass, field
import random

from game.characters.ICharacter_ren import ICharacter
from game.phone.kiwii.KiwiiComment_ren import KiwiiComment

kiwii_posts: list[KiwiiPost]

"""renpy
init python:
"""


@dataclass
class KiwiiPost:
    user: ICharacter
    image: str
    message: str = ""
    mentions: list[ICharacter] = field(default_factory=list)
    number_likes: int = random.randint(250, 500)
    liked: bool = False
    comments: list[KiwiiComment] = field(default_factory=list)
    pending_comments: list[KiwiiComment] = field(default_factory=list)
