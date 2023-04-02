"""renpy
init python:
"""

from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from renpy.exports import store
    import renpy.exports as renpy
    from game.phone.Application_ren import Application


class Phone:
    def __init__(self, *applications: Application) -> None:
        self.applications: tuple[Application] = applications

    @property
    def notification(self) -> bool:
        return any(app.notification for app in self.applications)

    @property
    def image(self) -> str:
        if self.notification:
            return "phone_icon"
        else:
            return "phone_icon_notification"

    @staticmethod
    def get_exit_actions():
        actions: list = [
            Hide("tutorial"),  # type: ignore
            Hide("message_reply"),  # type: ignore
            SetVariable("phone_from_phone_icon", False),  # type: ignore
        ]
        if (
            not store.phone_from_phone_icon
            and renpy.context()._current_interact_type == "screen"
        ):
            actions.append(Return())  # type: ignore
        else:
            actions.append(Hide("phone_tag"))  # type: ignore
        return actions
