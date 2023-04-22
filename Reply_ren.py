"""renpy
init python:
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from game.phone.MessengerBuilder_ren import MessageBuilder


@dataclass
class Reply:
    content: str
    next_message: Optional[MessageBuilder] = None

    def send(self) -> None:
        self.contact.text_messages.append(self)
