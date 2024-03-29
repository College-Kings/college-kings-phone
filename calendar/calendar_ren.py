from game.phone.Application_ren import Application

"""renpy
init python:
"""


class CalendarApp(Application, object):
    @property
    def name(self) -> str:
        return "Calendar"

    def clear_notifications(self) -> None:
        return None


calendar_app = CalendarApp()
