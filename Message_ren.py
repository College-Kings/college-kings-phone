from dataclasses import dataclass

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.characters.character_ren import Character
from game.characters.main_character_ren import MainCharacter
from game.phone.messenger.Reply_ren import Reply

mc = MainCharacter()

"""renpy
init python:
"""


@dataclass
class Message:
    contact: Character
    content: str
    replies: tuple["Reply", ...] = ()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.contact.name}, {self.content=}, {self.replies})"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Message):
            return NotImplemented

        return (
            self.contact == __value.contact
            and self.content == __value.content
            and self.replies == __value.replies
        )

    @classmethod
    def from_reply(cls, reply: "Reply") -> "Message":
        return cls(mc, reply.content, ())

    def send(self) -> None:
        if not isinstance(self.contact, NonPlayableCharacter):
            raise TypeError(
                f"Only NonPlayableCharacters can receive messages, not {self.contact}"
            )

        self.contact.text_messages.append(self)
