from dataclasses import dataclass, field
from typing import Any

from renpy.common.action_control import Hide, Return
import renpy.exports as renpy

from game.phone.messenger.Messenger_ren import Messenger
from game.phone.Application_ren import Application, Kiwii

messenger = Messenger()
achievement_app = Application("Achievements")
relationship_app = Application("Relationships")
kiwii = Kiwii()
reputation_app = Application("Reputation")
tracker = Application("Tracker")
calendar = Application("Calendar")

phone_from_phone_icon: bool

"""renpy
init python:
"""


@dataclass
class Phone:
    _applications: list[Application] = field(default_factory=list)

    @property
    def applications(self) -> list[Application]:
        try:
            self._applications
        except AttributeError:
            self.applications = [
                messenger,
                achievement_app,
                relationship_app,
                kiwii,
                reputation_app,
                tracker,
                calendar,
            ]

        if not self._applications:
            self.applications = [
                messenger,
                achievement_app,
                relationship_app,
                kiwii,
                reputation_app,
                tracker,
                calendar,
            ]

        return self._applications

    @applications.setter
    def applications(self, value: list[Application]) -> None:
        self._applications = value

    @property
    def notification(self) -> bool:
        return any(app.notification for app in self.applications)

    @property
    def icon(self) -> str:
        return "phone_icon"

    @property
    def image(self) -> str:
        if self.notification:
            return "phone_icon_notification"
        else:
            return "phone_icon"

    @staticmethod
    def get_exit_actions() -> list[Any]:
        actions: list[Any] = [
            Hide("tutorial"),
            SetVariable("phone_from_phone_icon", False),  # type: ignore
        ]
        if (
            not phone_from_phone_icon
            and renpy.context()._current_interact_type == "screen"  # type: ignore
        ):
            actions.append(Return())
        else:
            actions.append(Hide("phone_tag"))
        return actions


phone = Phone()
