from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiService_ren import KiwiiService

"""renpy
init python:
"""


class Application:
    def __init__(self, name: str) -> None:
        self.name: str = name

    @property
    def home_screen(self) -> str:
        return f"{self.name.lower()}_home"

    @property
    def image(self) -> str:
        if self.notification:
            return f"{self.name.lower()}_icon_notification"
        else:
            return f"{self.name.lower()}_icon"

    @property
    def notification(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name})"


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
