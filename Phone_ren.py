from __future__ import annotations
from typing import Any

import renpy.exports as renpy

from game.phone.Application_ren import Application

phone_from_phone_icon: bool

"""renpy
init python:
"""


class Phone:
    def __init__(self) -> None:
        self.applications: tuple[Application, ...] = ()

    @property
    def notification(self) -> bool:
        return any(app.notification for app in self.applications)

    @property
    def image(self) -> str:
        if self.notification:
            return "phone_icon_notification"
        else:
            return "phone_icon"

    @staticmethod
    def get_exit_actions() -> list[Any]:
        actions: list[Any] = [
            Hide("tutorial"),  # type: ignore
            Hide("message_reply"),  # type: ignore
            SetVariable("phone_from_phone_icon", False),  # type: ignore
        ]
        if (
            not phone_from_phone_icon
            and renpy.context()._current_interact_type == "screen"
        ):
            actions.append(Return())  # type: ignore
        else:
            actions.append(Hide("phone_tag"))  # type: ignore
        return actions


phone = Phone()
