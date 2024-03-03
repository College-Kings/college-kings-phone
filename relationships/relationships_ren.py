from game.phone.Application_ren import Application

"""renpy
init python:
"""


class Relationships(Application, object):
    def clear_notifications(self) -> None:
        return None


relationship_app = Relationships()
