"""renpy
init python:
"""

from typing import TYPE_CHECKING, Union


if TYPE_CHECKING:
    from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
    from game.phone.kiwii.KiwiiComment_ren import KiwiiComment
    from game.phone.kiwii.KiwiiPost_ren import KiwiiPost


class Application:
    def __init__(self) -> None:
        self.name: str = self.__class__.__name__
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
        super().__init__()

        self.contacts: list[NonPlayableCharacter] = []

    @property
    def notification(self) -> bool:
        return any(contact.pending_text_messages for contact in self.contacts)

    def move_contact_to_top(self, contact: NonPlayableCharacter) -> None:
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)


class Simplr(Application):
    def __init__(self) -> None:
        super().__init__()

        self.contacts: list[NonPlayableCharacter] = []
        self.pending_contacts: list[NonPlayableCharacter] = []

    @property
    def notification(self) -> bool:
        return any(contact.notification for contact in self.contacts)

    def move_contact_to_top(self, contact: NonPlayableCharacter) -> None:
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)


class Kiwii(Application):
    def __init__(self) -> None:
        super().__init__()

        self.posts: list[KiwiiPost] = []

    @property
    def notification(self) -> bool:
        for post in self.posts:
            if post.replies:
                return True
            try:
                if not post.seen:
                    return True
            except AttributeError:
                post.seen = True

        return False

    @staticmethod
    def get_message(kiwii_obj: Union[KiwiiComment, KiwiiPost]) -> str:
        usernames: list[str] = [mention.username for mention in kiwii_obj.mentions]

        message: str = ", @".join(usernames)
        if usernames:
            message: str = (
                f"{{color=#3498DB}}{{b}}@{message}{{/b}}{{/color}} {kiwii_obj.message}"
            )
        else:
            message = kiwii_obj.message

        return message

    @staticmethod
    def toggle_liked(kiwii_obj: Union[KiwiiComment, KiwiiPost]) -> None:
        kiwii_obj.liked = not kiwii_obj.liked

        try:
            kiwii_obj.number_likes
        except AttributeError:
            # noinspection PyUnresolvedReferences
            kiwii_obj.number_likes = kiwii_obj.numberLikes

        if kiwii_obj.liked:
            kiwii_obj.number_likes += 1
        else:
            kiwii_obj.number_likes -= 1