from game.phone.Application_ren import Application

"""renpy
init python:
"""


class Calendar(Application, object):
    def clear_notifications(self) -> None:
        return None


calendar = Calendar()
