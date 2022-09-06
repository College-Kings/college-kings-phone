screen calendar_home():
    tag phone_tag
    modal True

    default image_path = "images/phone/calendar/app-assets/"
    default temp_calendar = calendar_now
    default temp_day = datetime.datetime(2022, 8, 1) # Used for setting days of the week. Probably shouldn't touch.
    default selected_date = temp_calendar

    $ year = temp_calendar.strftime("%Y")
    $ month = temp_calendar.strftime("%B")
    $ day = temp_day.strftime("%a")
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
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year - 1, 12, temp_calendar.day))]
                
                elif temp_calendar.month > 1:
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month - 1, temp_calendar.day))]

            imagebutton:
                idle image_path + "button_right.png"
                if temp_calendar.month == 12:
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year + 1, 1, temp_calendar.day))]
                
                elif temp_calendar.month < 12:
                    action [SetScreenVariable("temp_calendar", datetime.datetime(temp_calendar.year, temp_calendar.month + 1, temp_calendar.day))]
        
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
            text "2/4": # To be replaced my task data count
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

                # Sets days for the month
                for i in range(1, month_range[1] + 1):
                    frame:
                        xysize (158, 122)

                        if i == calendar_now.day and temp_calendar.month == calendar_now.month and temp_calendar.year == calendar_now.year:
                            add image_path + "current_date.png" xalign 0.5 ypos -7

                        text "[i]" pos (16, 12) style "label_text"
                        
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