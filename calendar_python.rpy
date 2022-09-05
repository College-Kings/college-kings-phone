init python:
    class Calendar:
        MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        @staticmethod
        def is_leap_year(year: int):
            """Return True for leap years, False for non-leap years."""
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        @staticmethod
        def month_range(year: int, month: int):
            """Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
            year, month."""

            if not 1 <= month <= 12:
                raise Exception(f"bad month number {month}; must be 1-12")

            day1 = datetime.date(year, month, 1).weekday()
            number_of_days = Calendar.MONTH_DAYS[month] + (
                month == 2 and Calendar.is_leap_year(year)
            )
            return (day1, number_of_days)

        @staticmethod
        def add_todo(
            day: int,
            month: int,
            year: int,
            id_: str,
            display_name: str,
            description: str = "",
        ):
            calendar_item = CalendarItem(id_, display_name, description, year, month, day)
            calendar_checklist.setdefault((year, month, day), []).append(calendar_item)
            return calendar_item

        @staticmethod
        def complete_todo(id_: str):
            calendar_items[id_].completed = True

        @staticmethod
        def remove_todo(id_: str):
            item = calendar_items[id_]
            calendar_checklist[item.day, item.month, item.year].remove(item)
            del calendar_items[id_]

        @staticmethod
        def add_days(number_of_days=1):
            calendar_now += datetime.timedelta(days=number_of_days)

        @staticmethod
        def set_time(year: int, month: int, day: int):
            calendar_now = datetime.datetime(year, month, day)


    class CalendarItem:
        def __init__(
            self, id_: str, name: str, description: str, year: int, month: int, day: int
        ):
            self.id_ = id_
            self.name = name
            self.description = description

            self.year = year
            self.month = month
            self.day = day

            self.completed = False

            calendar_items[id_] = self


default calendar_items = {}
default calendar_checklist = {}