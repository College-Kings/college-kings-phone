screen messenger_home():
    tag phone_tag
    modal True

    add "darker_80"

    default exit_actions = Phone.get_exit_actions()

    # Click background to close phone
    button:
        sensitive True
        selected False
        action exit_actions

    textbutton _("Exit Phone"):
        style "phonebutton"
        sensitive True
        selected False
        action exit_actions

    frame:
        background "phone_screen"
        align (0.5, 0.5)
        xysize (433, 918)

        frame:
            background "messenger_home_background"
            xysize (433, 918)

            vpgrid:
                cols 1
                spacing 5
                mousewheel True
                draggable True
                pos (11, 134)
                xysize (416, 709)

                for contact in messenger.contacts:
                    button:
                        action [Function(renpy.retain_after_load), Show("messenger", contact=contact)]
                        ysize 80

                        add contact.profile_picture_65x65:
                            xpos 20
                            yalign 0.5

                        text contact.name:
                            style "nametext"
                            xpos 100
                            yalign 0.5

                        if MessengerService.has_replies(contact):
                            add "phone_contact_notification" align (1.0, 0.5) xoffset -25

        fixed:
            ysize 69
            ypos 843

            imagebutton:
                idle "phone_home_button_idle"
                hover "phone_home_button_hover"
                action Show("phone")
                align (0.5, 0.5)

    key [ "K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3" ]:
        action exit_actions


    if config_debug:
        for contact in messenger.contacts:
            if MessengerService.has_replies(contact):
                timer 0.1 action [Function(renpy.retain_after_load), Show("messenger", contact=contact)]
