from typing import Optional

from game.phone.messenger.MessageBuilder_ren import MessageBuilder
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.Message_ren import Message
from game.phone.messenger.Messenger_ren import Messenger
from game.phone.messenger.Reply_ren import Reply

messenger = Messenger()

"""renpy
init python:
"""


class MessengerService:
    @staticmethod
    def replies(contact: NonPlayableCharacter) -> list["Reply"]:
        messenger.add_contact(contact)

        try:
            return list(contact.text_messages[-1].replies)
        except (IndexError, AttributeError):
            return []

    @staticmethod
    def has_replies(contact: NonPlayableCharacter) -> bool:
        messenger.add_contact(contact)

        try:
            return bool(contact.text_messages[-1].replies)
        except (IndexError, AttributeError):
            return False

    @staticmethod
    def new_message(
        contact: NonPlayableCharacter,
        content: str,
        *replies: "Reply",
        clear_pending: bool = True,
    ) -> None:
        contact.pending_text_messages.append(Message(contact, content, replies))

        Messenger.send_next_messages(contact)

        messenger.new_notification(contact)

    @staticmethod
    def add_reply(
        contact: NonPlayableCharacter,
        content: str,
        next_message: Optional[MessageBuilder] = None,
    ) -> None:
        MessengerService.add_replies(contact, Reply(content, next_message))

    @staticmethod
    def add_replies(contact: NonPlayableCharacter, *replies: "Reply") -> None:
        if (
            not contact.pending_text_messages
            or contact.pending_text_messages[0].replies
        ):
            return MessengerService.new_message(contact, "", *replies)

        contact.pending_text_messages[-1].replies = replies

        messenger.new_notification(contact)

    @staticmethod
    def find_message(contact: NonPlayableCharacter, content: str) -> Optional[Message]:
        for message in contact.pending_text_messages + contact.text_messages:
            if message.content == content:
                return message

        return None
