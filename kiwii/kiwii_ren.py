from game.phone.Application_ren import Application
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiService_ren import KiwiiService

"""renpy
init python:
"""


class Kiwii(Application, object):
    def __init__(self) -> None:
        self.posts: list[KiwiiPost] = []

    @property
    def notification(self) -> bool:
        return any(KiwiiService.has_replies(post) for post in self.posts)

    def clear_notifications(self) -> None:
        return None
