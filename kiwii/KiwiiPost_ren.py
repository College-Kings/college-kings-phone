from __future__ import annotations
from dataclasses import dataclass, field
import random

from game.characters.ICharacter_ren import ICharacter
from game.phone.kiwii.KiwiiComment_ren import KiwiiComment

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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.user}, {self.message}, {self.comments})"
        )

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, KiwiiPost):
            return NotImplemented

        return (
            self.user == __value.user
            and self.image == __value.image
            and self.message == __value.message
        )
