# from abc import abstractmethod
from typing import Protocol

"""renpy
init python:
"""


class Application(Protocol):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def home_screen(self) -> str:
        return f"{self.name.lower()}_home"

    @property
    def icon(self) -> str:
        if self.notification:
            return f"{self.name.lower()}_icon_notification"
        else:
            return f"{self.name.lower()}_icon"

    @property
    def notification(self) -> bool:
        return False

    def clear_notifications(self) -> None:
        return None
