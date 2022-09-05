screen calendar_home():
    tag phone_tag

    default image_path = "images/phone/calendar/app-assets/"
    add image_path + "background.webp"
    add image_path + "frame.webp" align (0.5, 0.5)

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action Show("phone")

    frame:
        
        # Month Page Buttons
        hbox:
            pos (833, 121)
            spacing 610
            
            imagebutton:
                idle image_path + "button_left_idle.png"
                hover image_path + "button_left_hover.png"
                action NullAction()

            imagebutton:
                idle image_path + "button_right_idle.png"
                hover image_path + "button_right_hover.png"
                action NullAction()
        
        # Month
        hbox:
            text "July": #Replace with data
                style "calendar_text"
                align (0.5, 0.5)
                pos (1210, 155)

        # Task Label
        hbox:
            pos (240, 220)
            spacing 100
            
            text "Sunday, 10th July":
                style "label_text"
                align (0.5, 0.5)

            text "2/4":
                style "task_count_text"
                align (0.5, 0.5)                

        # Tasks
        vbox:
            pos (200, 520)
            spacing -95

            add image_path + "button_green.png" #Completed Task

            add image_path + "button_blue.webp" #Incomplete Task

        vbox:
            
            # Days of the week
            grid 7 1:
                pos (750, 230)
                spacing 85
                
                text "Mon" align (0.5, 0.5) style "label_text"
                text "Tue" align (0.5, 0.5) style "label_text"
                text "Wed" align (0.5, 0.5) style "label_text"
                text "Thu" align (0.5, 0.5) style "label_text"
                text "Fri" align (0.5, 0.5) style "label_text"
                text "Sat" align (0.5, 0.5) style "label_text"
                text "Sun" align (0.5, 0.5) style "label_text"

            # Dates
            grid 7 5:
                pos (720, 270)
                xspacing 113
                yspacing 103
                allow_underfull True

                for i in range(1, 31):
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