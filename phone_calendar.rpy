screen calendar_home():
    tag phone_tag

    default image_path = "images/phone/calendar/app-assets/"
    default temp_calendar = calendar_now

    $ year = temp_calendar.strftime("%Y")
    $ month = temp_calendar.strftime("%B")
    $ day = temp_calendar.strftime("%a")
    $ date = temp_calendar.strftime("%d")
    $ month_range = Calendar.month_range(temp_calendar.year, temp_calendar.month)

    add image_path + "background.webp"
    add image_path + "frame.png" align (0.5, 0.5)

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action Show("phone")

    frame:
        
        # Month Page Buttons
        hbox:
            pos (819, 75)
            spacing 680
            
            imagebutton:
                idle image_path + "button_left.png"
                if temp_calendar.month == 1:
                    action SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year-1, 12, temp_calendar.day))
                elif temp_calendar.month > 1:
                    action SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month-1, temp_calendar.day))

            imagebutton:
                idle image_path + "button_right.png"
                if temp_calendar.month == 12:
                    action SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year+1, 1, temp_calendar.day))
                elif temp_calendar.month < 12:
                    action SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month+1, temp_calendar.day))
        
        # Month
        text month:
            style "calendar_text"
            align (0.5, 0.5)
            pos (1230, 115)

        # Task Label
        hbox:
            pos (160, 200)
            
            text "[year], [date] [month]":
                style "label_text"
                align (0.5, 0.5)

        hbox:
            pos (520, 190)
            text "2/4":
                style "task_count_text"
                align (0.5, 0.5)                

        # Tasks
        vbox:
            pos (150, 250)
            spacing -25

            add image_path + "button_green.webp" #Completed Task

            add image_path + "button_blue.png" #Incomplete Task

        vbox:
            
            # Days of the week
            grid 7 1:
                pos (730, 200)
                spacing 100
                
                text "Mon" align (0.5, 0.5) style "label_text"
                text "Tue" align (0.5, 0.5) style "label_text"
                text "Wed" align (0.5, 0.5) style "label_text"
                text "Thu" align (0.5, 0.5) style "label_text"
                text "Fri" align (0.5, 0.5) style "label_text"
                text "Sat" align (0.5, 0.5) style "label_text"
                text "Sun" align (0.5, 0.5) style "label_text"

            # Dates - Fill from "calendar_now" data
            grid 7 6:
                pos (685, 240)
                xspacing 129
                yspacing 93
                allow_underfull True
                

                for i in range(0, month_range[0]):
                    text "[i]" align (0.5, 0.5) style "inv_label_text"

                for i in range(1, month_range[1]+1):
                    text "[i]" align (0.5, 0.5) style "label_text"


style calendar_text is text:
    color "#fff"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 54

style task_count_text is text:
    color "#fff"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 39

style label_text is text:
    color "#ffffff60"
    font "fonts/Montserrat-SemiBold.ttf"
    size 24

style inv_label_text is text:
    color "#ffffff00"
    font "fonts/Montserrat-SemiBold.ttf"
    size 24