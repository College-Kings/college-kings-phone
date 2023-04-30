from __future__ import annotations

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.Message_ren import Message
from game.phone.Reply_ren import Reply

from renpy import store

"""renpy
init python:
"""


class MessengerService:
    @staticmethod
    def has_replies(contact: NonPlayableCharacter) -> bool:
        return (
            contact.text_messages
            and hasattr(contact.text_messages[-1], "replies")
            and contact.text_messages[-1].replies
        )

    @staticmethod
    def send_next_messages(contact: NonPlayableCharacter) -> None:
        while contact.pending_text_messages and not MessengerService.has_replies(
            contact
        ):
            contact.pending_text_messages.pop(0).send()

    @staticmethod
    def new_message(
        contact: NonPlayableCharacter, content: str, *replies: Reply, clear_pending=True
    ) -> None:
        contact.pending_text_messages.append(Message(contact, content, replies))

        store.messenger.move_contact_to_top(contact)

        MessengerService.send_next_messages(contact)

    @staticmethod
    def add_reply(
        contact: NonPlayableCharacter, content: str, next_message=None
    ) -> None:
        MessengerService.add_replies(contact, Reply(content, next_message))

    @staticmethod
    def add_replies(contact: NonPlayableCharacter, *replies: Reply) -> None:
        if (
            not contact.pending_text_messages
            or contact.pending_text_messages[0].replies
        ):
            return MessengerService.new_message(contact, "", *replies)

        contact.pending_text_messages[-1].replies = replies

    @staticmethod
    def find_message(contact: NonPlayableCharacter, content: str) -> Message:
        for message in contact.pending_text_messages + contact.text_messages:
            if message.content == content:
                return message

        return None
