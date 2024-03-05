from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.Application_ren import Application

"""renpy
init python:
"""


class Simplr(Application, object):
    def __init__(self) -> None:
        self.pending_contacts: list[NonPlayableCharacter] = []

    def clear_notifications(self) -> None:
        return None
