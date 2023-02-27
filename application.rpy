init python:
    class Application:
        def __init__(self, name: str):
            self.name = name
            self.home_screen = f"{self.name.lower()}_home"

            self.contacts: list[Contact] = []

        def __repr__(self):
            return f"{type(self).__name__}({self.name})"

        @property
        def image(self):
            if self.notification:
                return f"images/phone/{self.name.lower()}/app-assets/icon-notification.webp"
            else:
                return f"images/phone/{self.name.lower()}/app-assets/icon.webp"

        @property
        def notification(self):
            return False

        def unlock(self):
            if self not in phone.applications:
                phone.applications.append(self)


    class Messenger(Application):
        def __init__(self):
            super().__init__("Messenger")

        @property
        def notification(self):
            return any(contact.notification for contact in self.contacts)

        @notification.setter
        def notification(self, value: Any):
            pass


    class Simplr(Application):
        def __init__(self):
            super().__init__("Simplr")

            self.pending_contacts = []

        @property
        def notification(self):
            return any(contact.notification for contact in self.contacts)

        @notification.setter
        def notification(self, value: Any):
            return


    class Kiwii(Application):
        def __init__(self):
            super().__init__("Kiwii")

        @property
        def notification(self):
            for post in kiwii_posts:
                if post.replies:
                    return True
                try:
                    if not post.seen:
                        return True
                except AttributeError:
                    post.seen = True

            return False

        @notification.setter
        def notification(self, value: Any):
            return

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


default messenger = Messenger()
default achievement_app = Application(_("Achievements"))
default kiwii = Kiwii()
default simplr_app = Simplr()
default relationship_app = Application(_("Relationships"))
default tracker = Application(_("Tracker"))
default reputation_app = Application(_("Reputation"))
default calendar = Application(_("Calendar"))