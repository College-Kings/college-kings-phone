from __future__ import annotations
from dataclasses import dataclass, field
import random

from game.characters.ICharacter_ren import ICharacter
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiReply_ren import KiwiiReply

"""renpy
init python:
"""


@dataclass
class KiwiiComment:
    post: KiwiiPost
    user: ICharacter
    message: str
    mentions: list[ICharacter] = field(default_factory=list)
    number_likes: int = random.randint(250, 500)
    liked: bool = False
    replies: tuple[KiwiiReply, ...] = ()

    def send(self) -> None:
        self.post.comments.append(self)
