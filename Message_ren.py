"""renpy
init python:
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
    from game.phone.Reply_ren import Reply


@dataclass
class Message:
    contact: NonPlayableCharacter
    content: str
    replies: list[Reply] = field(default_factory=list)

    def send(self):
        self.contact.text_messages.append(self)
