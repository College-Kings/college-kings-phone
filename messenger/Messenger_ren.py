from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.characters.character_ren import Character
from game.phone.Application_ren import Application
from game.phone.messenger.MessengerService_ren import MessengerService

"""renpy
init python:
"""


class Messenger(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.contacts: list[Character] = []

    @property
    def notification(self) -> bool:
        return any(
            MessengerService.has_replies(contact)
            for contact in self.contacts
            if isinstance(contact, NonPlayableCharacter)
        )

    def add_contact(self, contact: NonPlayableCharacter) -> None:
        if contact not in self.contacts:
            print(f"Adding {contact}")
            self.contacts.append(contact)

    def move_contact_to_top(self, contact: NonPlayableCharacter) -> None:
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)
