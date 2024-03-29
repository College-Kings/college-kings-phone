from game.phone.Application_ren import Application

"""renpy
init python:
"""


class Tracker(Application, object):

    def clear_notifications(self) -> None:
        return None


tracker = Tracker()
