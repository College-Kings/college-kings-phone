from game.phone.Application_ren import Application

"""renpy
init python:
"""


class Achievements(Application, object):
    def clear_notifications(self) -> None:
        return None


achievements_app = Achievements()
