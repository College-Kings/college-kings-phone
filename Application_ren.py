"""renpy
init python:
"""


class Application:
    def __init__(self, name: str):
        self.name = name
        self.home_screen = f"{self.name.lower()}_home"

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"

    @property
    def image(self):
        if self.notification:
            return f"{self.name.lower()}_icon_notification"
        else:
            return f"{self.name.lower()}_icon"

    @property
    def notification(self):
        return False

    def unlock(self):
        if self not in phone.applications:
            phone.applications.append(self)


class Messenger(Application):
    def __init__(self):
        super().__init__("Messenger")

        self.contacts: list[NonPlayableCharacter] = []

    @property
    def notification(self):
        return any(contact.pending_text_messages for contact in self.contacts)

    def move_contact_to_top(self, contact: NonPlayableCharacter):
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)


class Simplr(Application):
    def __init__(self):
        super().__init__("Simplr")

        self.contacts: list[Contact] = []
        self.pending_contacts = []

    @property
    def notification(self):
        return any(contact.notification for contact in self.contacts)


class Kiwii(Application):
    def __init__(self):
        super().__init__("Kiwii")

        self.posts: list[KiwiiPost] = []

    @property
    def notification(self):
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
    def get_message(kiwii_obj: Union[KiwiiComment, KiwiiPost]):
        usernames = [mention.username for mention in kiwii_obj.mentions]

        message = ", @".join(usernames)
        if usernames:
            message = (
                f"{{color=#3498DB}}{{b}}@{message}{{/b}}{{/color}} {kiwii_obj.message}"
            )
        else:
            message = kiwii_obj.message

        return message

    @staticmethod
    def toggle_liked(kiwii_obj: Union[KiwiiComment, KiwiiPost]):
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
