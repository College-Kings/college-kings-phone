from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.characters.character_ren import Character
from game.phone.Application_ren import Application
from game.phone.Phone_ren import Phone

phone: Phone

"""renpy
init python:
"""


class Messenger(Application, object):
    def __init__(self) -> None:
        self.contacts: list[Character] = []
        self.notifications: set[NonPlayableCharacter] = set()

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
