from __future__ import annotations
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
