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
    number_likes: int = random.randint(250, 500)
    mentions: list[ICharacter] = field(default_factory=list)
    liked: bool = False
    replies: tuple[KiwiiReply, ...] = ()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.user}, {self.message}, {self.replies})"

    def send(self) -> None:
        self.post.comments.append(self)
