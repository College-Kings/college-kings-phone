from typing import Any
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.characters.base_character_ren import BaseCharacter
from game.phone.Application_ren import Application
from game.phone.Message_ren import Message
from game.phone.Phone_ren import Phone
from game.phone.messenger.MessengerService_ren import MessengerService

import renpy.exports as renpy

phone: Phone

"""renpy
init python:
"""


class Messenger(Application, object):
    def __init__(self) -> None:
        self.contacts: list[BaseCharacter] = []
        self.notifications: set[NonPlayableCharacter] = set()

    def __repr__(self) -> str:
        contacts_repr = ", ".join(
            [
                f"{contact.__class__.__name__}({contact.name})"
                for contact in self.contacts
            ]
        )
        return f"{self.__class__.__name__}({self.name}, self.contacts=[{contacts_repr}], {self.notifications=})"

    @property
    def notification(self) -> bool:
        try:
            self.notifications
        except AttributeError:
            self.notifications = set()

        return bool(self.notifications)

    def add_contact(self, contact: NonPlayableCharacter) -> None:
        if contact not in self.contacts:
            self.contacts.append(contact)

    def move_contact_to_top(self, contact: NonPlayableCharacter) -> None:
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)

    def clear_notifications(self) -> None:
        self.notifications.clear()

    def new_notification(self, contact: NonPlayableCharacter) -> None:
        self.move_contact_to_top(contact)
        self.notifications.add(contact)

    def remove_notification(self, contact: NonPlayableCharacter) -> None:
        if contact in self.notifications:
            self.notifications.remove(contact)

    @staticmethod
    def send_next_messages(contact: NonPlayableCharacter) -> None:
        while contact.pending_text_messages and not MessengerService.has_replies(
            contact
        ):
            contact.pending_text_messages.pop(0).send()


class SendReply:
    def __init__(self, contact: NonPlayableCharacter, reply_index: int) -> None:
        self.contact = contact
        self.reply_index = reply_index

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        last_message = self.contact.text_messages[-1]

        try:
            reply = last_message.replies[self.reply_index]
        except IndexError:
            print(f"Invalid reply index: {self.reply_index}")
            return

        last_message.replies = ()
        if last_message.content == "":
            del self.contact.text_messages[-1]

        self.contact.text_messages.append(Message.from_reply(reply))

        if reply.next_message is None:
            Messenger.send_next_messages(self.contact)
        else:
            reply.next_message.send()

        renpy.restart_interaction()
