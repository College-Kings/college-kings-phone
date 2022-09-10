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
            year: int,
            month: int,
            day: int,
            id_: str,
            display_name: str,
            description: str = "",
        ):
            calendar_item = CalendarItem(id_, display_name, description, year, month, day)
            calendar_checklist.setdefault((year, month, day), []).append(calendar_item)
            return calendar_item

        @staticmethod
        def complete_todo(id_: str):
            calendar_item = calendar_items[id_]
            calendar_item.completed = True
            return calendar_item

        @staticmethod
        def remove_todo(id_: str):
            item = calendar_items[id_]
            calendar_checklist[item.day, item.month, item.year].remove(item)
            del calendar_items[id_]

        @staticmethod
        def add_days(number_of_days: int = 1):
            calendar_now += datetime.timedelta(days=number_of_days)

        @staticmethod
        def set_time(year: int, month: int, day: int):
            calendar_now = datetime.datetime(year, month, day)

        @staticmethod
        def contains(id_: str):
            return id_ in calendar_item

        @staticmethod
        def find(id_: str):
            return calendar_item.get(id_, None)


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


screen calendar_home():
    tag phone_tag
    modal True

    default image_path = "images/phone/calendar/app-assets/"
    default temp_calendar = calendar_now
    default selected_date = calendar_now
    
    python:
        list_count = len(calendar_checklist.get((selected_date.year, selected_date.month, selected_date.day), []))
        count_complete = len([
                calendar_item
                for calendar_item in calendar_checklist.get((selected_date.year, selected_date.month, selected_date.day), [])
                if calendar_item.completed
            ])
   
        month_range = Calendar.month_range(temp_calendar.year, temp_calendar.month)

    add image_path + "background.webp"
    add image_path + "frame.webp" align (0.5, 0.5)

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action Show("phone")

    frame:
        xysize (838, 79)
        pos (819, 75)

        # Month page buttons
        imagebutton:
            idle image_path + "button_left.webp"
            if temp_calendar.month == 1:
                action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year - 1, 12, 1))]
            else:
                action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month - 1, 1))]
            yalign 0.5

        imagebutton:
            idle image_path + "button_right.webp"
            if temp_calendar.month == 12:
                action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year + 1, 1, 1))]
            else:
                action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month + 1, 1))]
            align (1.0, 0.5)

        # Month label
        text temp_calendar.strftime("%B"):
            style "calendar_text"
            align (0.5, 0.5)

    frame:
        xysize (500, 670)
        pos (123, 162)

        frame:
            xfill True
            ysize 100
            padding (35, 0)

            # Task label
            text selected_date.strftime("%Y, %d, %B"):
                style "label_text"
                yalign 0.5

            # Task count
            text "[count_complete]/[list_count]":
                style "task_count_text"
                align (1.0, 0.5)

        # Tasks
        vbox:
            xfill True
            ypos 100
            spacing -25
            
            for task in calendar_checklist.get((selected_date.year, selected_date.month, selected_date.day), []):
                frame:
                    xysize (436, 143)
                    if task.completed:
                        background image_path + "button_green.webp"
                    else:
                        background image_path + "button_blue.webp"

                    text task.description:
                        style "task_icon_text"
                        xpos 40
                        yalign 0.5
                        xsize 300

    # Calendar Setup
    frame:
        xysize (1117, 843)
        pos (680, 162)

        # Days of the week
        frame:
            xfill True
            ysize 100

            grid 7 1:
                xfill True
                yalign 0.5

                for day in ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"):
                    text day:
                        style "label_text"
                        xalign 0.5
        
        # Dates
        grid 7 6:
            ypos 100
            spacing 2
            allow_underfull True
            
            # Gives blank space to offset month start date
            for i in range(0, month_range[0]):
                null width 158 height 122

            # Sets dates for the month
            for i in range(1, month_range[1] + 1):
                python:
                    number_task_complete = 0
                    number_task_incomplete = 0

                    for task in calendar_checklist.get((temp_calendar.year, temp_calendar.month, i), []):
                        if task.completed:
                            number_task_complete += 1
                        else:
                            number_task_incomplete += 1

                frame:
                    xysize (158, 122)

                    if i == calendar_now.day and temp_calendar.month == calendar_now.month and temp_calendar.year == calendar_now.year:
                        add image_path + "current_date.webp" xalign 0.5 ypos -7

                    text "[i]" pos (5, 1) style "label_text"
                    
                    if i == selected_date.day and temp_calendar.month == selected_date.month and temp_calendar.year == selected_date.year:
                        add image_path + "date_select.webp"
                            
                    else:
                        imagebutton:
                            idle "#0000"
                            hover image_path + "date_select.webp"
                            action [SetScreenVariable("selected_date", datetime.datetime(temp_calendar.year, temp_calendar.month, i))]
                            align (0.5, 0.5)

                    # Icons for completed/incomplete tasks
                    vbox:
                        align (0.5, 1.0)
                        yoffset -5
                        spacing -10

                        if (temp_calendar.year, temp_calendar.month, i) in calendar_checklist:
                            frame:
                                xysize (117, 55)
                                background image_path + "incomplete_icon.webp"

                                text "[number_task_complete]" style "task_icon_text" align (0.5, 0.5)

                            frame:
                                xysize (117, 55)
                                background image_path + "complete_icon.webp"
                            
                                text "[number_task_incomplete]" style "label_text" align (0.5, 0.5)

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")


style calendar_text is text:
    color "#fff"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 54

style task_count_text is text:
    color "#fff"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 39

style task_icon_text is text:
    color "#fff"
    font "fonts/Montserrat-SemiBold.ttf"
    size 24

style label_text is text:
    color "#ffffff60"
    font "fonts/Montserrat-SemiBold.ttf"
    size 24

style inv_label_text is text:
    color "#ffffff00"
    font "fonts/Montserrat-SemiBold.ttf"
    size 24