from dataclasses import dataclass
from typing import Optional

from game.phone.messenger.MessageBuilder_ren import MessageBuilder

"""renpy
init python:
"""


@dataclass
class Reply:
    content: str
    next_message: Optional[MessageBuilder] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.content})"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Reply):
            return NotImplemented

        return self.content == __value.content
