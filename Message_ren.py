from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
    from game.phone.messenger.Reply_ren import Reply

"""renpy
init python:
"""


@dataclass
class Message:
    contact: NonPlayableCharacter
    content: str
    replies: tuple[Reply, ...] = ()

    def send(self) -> None:
        self.contact.text_messages.append(self)
