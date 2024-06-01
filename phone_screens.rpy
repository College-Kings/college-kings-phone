default phone_from_phone_icon = False


screen phone_icon():
    zorder 10

    imagebutton:
        idle phone.icon
        action (SetVariable("phone_from_phone_icon", True), Show("phone"), If(persistent.enabled_tutorials["phone_tutorial"], Show("phone_tutorial")))
        xalign 1.0
        offset (25, -25)


screen base_phone(background="phone_screen"):
    modal True

    add "darker_80"

    $ exit_actions = Phone.get_exit_actions()

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
        modal True
        background background
        align (0.5, 0.5)
        xysize (433, 918)

        transclude

        if not renpy.get_screen("phone"):
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


screen base_phone_rotated():
    modal True

    add "darker_80"

    # Click background to close phone
    button:
        action Phone.get_exit_actions()

    textbutton _("Exit Phone"):
        style "phonebutton"
        action Phone.get_exit_actions()

    frame:
        align (0.5, 0.5)
        xysize (918, 433)

        transclude

        fixed:
            xsize 69
            xpos 844

            imagebutton:
                idle "phone_home_button_idle"
                hover "phone_home_button_hover"
                action Show("phone")
                align (0.5, 0.5)

    key [ "K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3" ]:
        action Phone.get_exit_actions()

# BUG: The phone screen causes lag when predicting 
screen phone():
    tag phone_tag
    modal True
    predict False

    use base_phone:
        vpgrid:
            cols 3
            spacing 35
            xalign 0.5
            ypos 100
            allow_underfull True

            for app in phone.applications:
                vbox:
                    spacing 2

                    imagebutton:
                        idle app.icon
                        action [Function(renpy.retain_after_load), Show(app.home_screen)]

                    text app.name style "application_name" xalign 0.5

    if config_debug:
        for app in phone.applications:
            if app.notification:
                timer 0.1 action [Function(renpy.retain_after_load), Show(app.home_screen)]

        if not any(app.notification for app in phone.applications):
            timer 0.1:
                action Phone.get_exit_actions()