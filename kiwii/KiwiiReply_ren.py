from __future__ import annotations
from dataclasses import dataclass, field
import random
from typing import Callable, Optional, Union


from game.characters.PlayableCharacters_ren import PlayableCharacter, mc
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost

"""renpy
init python:
"""


@dataclass
class KiwiiReply:
    message: str
    func: Optional[Callable[[KiwiiPost], None]] = None
    number_likes: int = random.randint(250, 500)
    mentions: list[Union[NonPlayableCharacter, PlayableCharacter]] = field(
        default_factory=list
    )

    liked: bool = False
    replies: list[KiwiiReply] = field(default_factory=list)
    reply: Optional[KiwiiReply] = None

    def __post_init__(self) -> None:
        self.user: PlayableCharacter = mc
