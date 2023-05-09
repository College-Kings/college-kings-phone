from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.messenger.MessengerService_ren import MessengerService
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiService_ren import KiwiiService

"""renpy
init python:
"""


class Application:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.home_screen: str = f"{self.name.lower()}_home"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name})"

    @property
    def image(self) -> str:
        if self.notification:
            return f"{self.name.lower()}_icon_notification"
        else:
            return f"{self.name.lower()}_icon"

    @property
    def notification(self) -> bool:
        return False


class Messenger(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.contacts: list[NonPlayableCharacter] = []

    @property
    def notification(self) -> bool:
        return any(MessengerService.has_replies(contact) for contact in self.contacts)

    def move_contact_to_top(self, contact: NonPlayableCharacter) -> None:
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)


class Simplr(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.pending_contacts: list[NonPlayableCharacter] = []


class Kiwii(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.posts: list[KiwiiPost] = []

    @property
    def notification(self) -> bool:
        return any(KiwiiService.has_replies(post) for post in self.posts)


messenger: Messenger
achievement_app: Application
relationship_app: Application
kiwii: Kiwii
reputation_app: Application
tracker: Application
calendar: Application
