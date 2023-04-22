"""renpy
init python:
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from game.phone.Message_ren import Message
from game.phone.Reply_ren import Reply

if TYPE_CHECKING:
    from renpy.exports import store
    from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter


class SimplrService:
    @staticmethod
    def has_replies(contact: NonPlayableCharacter) -> bool:
        return (
            contact.simplr_messages
            and hasattr(contact.simplr_messages[-1], "replies")
            and contact.simplr_messages[-1].replies
        )

    @classmethod
    def send_next_messages(cls, contact: NonPlayableCharacter) -> None:
        while contact.pending_simplr_messages and not cls.has_replies(contact):
            contact.pending_simplr_messages.pop(0).send()

    @classmethod
    def new_message(
        cls,
        contact: NonPlayableCharacter,
        content: str,
        *replies: Reply,
        clear_pending=True,
    ) -> None:
        contact.pending_simplr_messages.append(Message(contact, content, replies))

        store.simplr.move_contact_to_top(contact)

        cls.send_next_messages(contact)

    @classmethod
    def add_reply(cls, contact: NonPlayableCharacter, content: str) -> None:
        cls.add_replies(contact, Reply(content))

    @classmethod
    def add_replies(cls, contact: NonPlayableCharacter, *replies: Reply) -> None:
        if (
            not contact.pending_simplr_messages
            or contact.pending_simplr_messages[0].replies
        ):
            return cls.new_message(contact, "", *replies)

        contact.pending_simplr_messages.replies = replies
