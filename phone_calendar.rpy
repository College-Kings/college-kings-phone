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


screen calendar_home():
    tag phone_tag
    modal True

    default image_path = "images/phone/calendar/app-assets/"
    default temp_calendar = calendar_now
    default temp_day = datetime.datetime(2022, 8, 1) # Used for setting days of the week. Probably shouldn't touch.
    default selected_date = temp_calendar
    
    python:
        count_complete = 0
        count_incomplete = 0

        if (selected_date.year, selected_date.month, selected_date.day) in calendar_checklist:
            count_complete = len([
                calendar_item
                for calendar_item in calendar_checklist[(selected_date.year, selected_date.month, selected_date.day)]
                if calendar_item.completed
            ])
            
            count_incomplete = len([
                calendar_item
                for calendar_item in calendar_checklist[(selected_date.year, selected_date.month, selected_date.day)]
                if not calendar_item.completed
            ])
    
    $ list_count = count_complete + count_incomplete
    $ year = selected_date.strftime("%Y")
    $ month = selected_date.strftime("%B")
    $ day = temp_day.strftime("%a")
    $ date = selected_date.strftime("%d")
    $ month_range = Calendar.month_range(temp_calendar.year, temp_calendar.month)
    

    add image_path + "background.webp"
    add image_path + "frame.png" align (0.5, 0.5)

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action Show("phone")

    frame:
        
        # Month page buttons
        hbox:
            pos (819, 75)
            spacing 680
            
            imagebutton:
                idle image_path + "button_left.png"
                if temp_calendar.month == 1:
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year - 1, 12, temp_calendar.day))]
                
                elif temp_calendar.month > 1:
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month - 1, temp_calendar.day))]

            imagebutton:
                idle image_path + "button_right.png"
                if temp_calendar.month == 12:
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year + 1, 1, temp_calendar.day))]
                
                elif temp_calendar.month < 12:
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month + 1, temp_calendar.day))]
        
        # Month label
        text temp_calendar.strftime("%B"):
            style "calendar_text"
            align (0.5, 0.5)
            pos (1230, 115)

        # Task label
        hbox:
            pos (160, 200)
            
            text "[year], [date] [month]":
                style "label_text"
                align (0.5, 0.5)

        # Task count
        hbox:
            pos (520, 190)

            text "[count_complete]/[list_count]":
                style "task_count_text"
                align (0.5, 0.5)                

        # Tasks
        vbox:
            pos (150, 250)
            spacing -25
            
            #Completed Tasks
            for i in range(count_complete):
                
                frame:
                    xysize (436, 143)
                    
                    add image_path + "button_green.webp"

                    $ description = calendar_checklist[selected_date.year, selected_date.month, selected_date.day][i].description

                    text "[description]" style "task_icon_text" xpos 40 yalign 0.5 xsize 300
                
            #Incomplete Tasks
            for i in range(count_incomplete):
                frame:
                    xysize (436, 143)
                    
                    add image_path + "button_blue.png"

                    $ description = calendar_checklist[selected_date.year, selected_date.month, selected_date.day][i].description

                    text "[description]" style "task_icon_text" xpos 40 yalign 0.5 xsize 300

        # Calendar Setup
        vbox:
            
            # Days of the week
            grid 7 1:
                pos (730, 200)
                spacing 100
                
                for i in range(1, 8):
                    text "[day]" align (0.5, 0.5) style "label_text"

                    $ day = datetime.datetime(temp_day.year, temp_day.month, temp_day.day + i).strftime("%a")

            # Dates
            grid 7 6:
                pos (683, 234)
                xspacing 1
                yspacing 1
                allow_underfull True
                
                # Gives blank space to offset month start date
                for i in range(0, month_range[0]):
                    frame:
                        xysize (158, 122)
                        text "[i]" align (0.5, 0.5) style "inv_label_text"

                # Sets dates for the month
                for i in range(1, month_range[1] + 1):
                    frame:
                        xysize (158, 122)

                        if i == calendar_now.day and temp_calendar.month == calendar_now.month and temp_calendar.year == calendar_now.year:
                            add image_path + "current_date.png" xalign 0.5 ypos -7

                        text "[i]" pos (5, 1) style "label_text"
                        
                        if i == selected_date.day and temp_calendar.month == selected_date.month and temp_calendar.year == selected_date.year:
                            imagebutton:
                                idle image_path + "date_select.png"
                                action NullAction()
                                align (0.5, 0.5)
                                
                        else:
                            imagebutton:
                                idle image_path + "date_select_idle.png"
                                hover image_path + "date_select.png"
                                action [SetScreenVariable("selected_date", datetime.datetime(temp_calendar.year, temp_calendar.month, i))]
                                align (0.5, 0.5)

                        # Icons for completed/incomplete tasks
                        vbox:
                            xpos 35
                            ypos 15
                            spacing -5

                            if (temp_calendar.year, temp_calendar.month, i) in calendar_checklist:
                                
                                add image_path + "incomplete_icon.png"

                                add image_path + "complete_icon.png"

                        # Count for tasks
                        vbox:
                            xpos 87
                            ypos 28
                            spacing 18

                            if (temp_calendar.year, temp_calendar.month, i) in calendar_checklist:
                                python:
                                    number_task_complete = 0
                                    number_task_incomplete = 0

                                    for task in calendar_checklist[(temp_calendar.year, temp_calendar.month, i)]:
                                        if task.completed:
                                            number_task_complete += 1
                                        else:
                                            number_task_incomplete += 1

                                text "[list_complete]" style "task_icon_text"

                                text "[list_incomplete]" style "label_text"

                                

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