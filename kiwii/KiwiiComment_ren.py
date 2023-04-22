"""renpy
init python:
"""

from __future__ import annotations
from dataclasses import dataclass, field
import random
from typing import Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from game.characters.PlayableCharacters_ren import PlayableCharacter
    from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
    from game.phone.kiwii.KiwiiReply_ren import KiwiiReply


@dataclass
class KiwiiComment:
    user: Union[PlayableCharacter, NonPlayableCharacter]
    message: str
    number_likes: int = random.randint(250, 500)
    mentions: list[Union[NonPlayableCharacter, PlayableCharacter]] = field(
        default_factory=list
    )
    liked: bool = False
    replies: list[KiwiiReply] = field(default_factory=list)
    reply: Optional[KiwiiReply] = None
