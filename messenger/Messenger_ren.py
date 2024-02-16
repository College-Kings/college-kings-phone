from game.characters.CharacterService_ren import CharacterService
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.Application_ren import Application
from game.phone.messenger.MessengerService_ren import MessengerService

"""renpy
init python:
"""


class Messenger(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self._contacts: list[NonPlayableCharacter] = []

    @property
    def contacts(self) -> list[NonPlayableCharacter]:
        try:
            self._contacts
        except AttributeError:
            old_contacts = self.__dict__.get("contacts", [])
            self._contacts = [i for i in old_contacts]

        try:
            self._contacts
        except AttributeError:
            self._contacts = []

        old_contacts = [i for i in self._contacts]
        self._contacts = []
        for contact in old_contacts:
            self._contacts.append(CharacterService.get_user(contact))

        return self._contacts

    @contacts.setter
    def contacts(self, value: list[NonPlayableCharacter]) -> None:
        self._contacts = value

    @property
    def notification(self) -> bool:
        return any(MessengerService.has_replies(contact) for contact in self.contacts)

    def add_contact(self, contact: NonPlayableCharacter) -> None:
        if contact not in self.contacts:
            self.contacts.append(contact)

    def move_contact_to_top(self, contact: NonPlayableCharacter) -> None:
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)
