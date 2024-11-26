from dataclasses import dataclass, field
import random
from typing import Sequence

from game.characters.base_character_ren import BaseCharacter
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiReply_ren import KiwiiReply

"""renpy
init python:
"""


@dataclass
class KiwiiComment:
    post: "KiwiiPost"
    user: BaseCharacter
    message: str
    number_likes: int = random.randint(250, 500)
    mentions: Sequence[BaseCharacter] = field(default_factory=list)
    liked: bool = False
    replies: tuple["KiwiiReply", ...] = ()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.user}, {self.message}, {self.replies})"

    def send(self) -> None:
        self.post.comments.append(self)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, KiwiiComment):
            return NotImplemented

        return (
            self.post == __value.post
            and self.user == __value.user
            and self.message == __value.message
        )
