from typing import Any

from game.phone.achievements.achievements_ren import achievements_app
from game.phone.kiwii.kiwii_ren import Kiwii
from game.phone.messenger.Messenger_ren import Messenger
from game.phone.relationships.relationships_ren import relationship_app
from game.phone.reputation.reputation_app_ren import reputation_app
from game.phone.simplr.simplr_ren import Simplr
from game.phone.Application_ren import Application

from renpy.common.action_control import Hide, Return
import renpy.exports as renpy

messenger = Messenger()
kiwii = Kiwii()
simplr_app = Simplr()

phone_from_phone_icon: bool

"""renpy
init python:
"""


class Phone:
    def __init__(self) -> None:
        self.applications: list[Application] = [
            messenger,
            achievements_app,
            relationship_app,
            kiwii,
            reputation_app,
        ]

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__init__()

        self.__dict__.update(state)

    @property
    def notifications(self) -> tuple[Application, ...]:
        return tuple(app for app in self.applications if app.notification)

    @property
    def notification(self) -> bool:
        return bool(self.notifications)

    @property
    def icon(self) -> str:
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

    def clear_notifications(self) -> None:
        for app in self.notifications:
            app.clear_notifications()
