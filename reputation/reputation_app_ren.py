from game.phone.Application_ren import Application

"""renpy
init python:
"""


class ReputationApp(Application, object):
    @property
    def home_screen(self) -> str:
        return "reputation_home"

    @property
    def icon(self) -> str:
        return "reputation_icon"

    def clear_notifications(self) -> None:
        return None


reputation_app = ReputationApp()
