init python:
    class Phone:
        def __init__(self, *applications):
            self.applications = applications

        @property
        def notification(self):
            return any(app.notification for app in self.applications)

        @property
        def image(self):
            if self.notification:
                return "phone_icon"
            else:
                return "phone_icon_notification"

        @staticmethod
        def get_exit_actions():
            actions = [Hide("tutorial"), Hide("message_reply"), SetVariable("phone_from_phone_icon", False)]
            if not phone_from_phone_icon and renpy.context()._current_interact_type == "screen":
                actions.append(Return())
            else:
                actions.append(Hide("phone_tag"))
            return actions


default phone_from_phone_icon = False


screen phone_icon():
    imagebutton:
        idle phone.image
        action [SetVariable("phone_from_phone_icon", True), Show("phone")]
        xalign 1.0
        offset (25, -25)


screen base_phone(background="phone_screen"):
    modal True

    add "darker_80"

    # Click background to close phone
    button:
        action Phone.get_exit_actions()

    textbutton _("Exit Phone"):
        style "phonebutton"
        action Phone.get_exit_actions()

    frame:
        background background
        align (0.5, 0.5)
        xysize (433, 918)
        modal True

        transclude

        if not renpy.get_screen("phone"):
            fixed:
                ysize 69
                ypos 843

                imagebutton:
                    idle "phone_home_button_idle"
                    hover "phone_home_button_hover"
                    action [Hide("message_reply"), Show("phone")]
                    align (0.5, 0.5)

    key [ "K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3" ]:
        action Phone.get_exit_actions()


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
        modal True

        transclude

        fixed:
            xsize 69
            xpos 844

            imagebutton:
                idle "phone_home_button_idle"
                hover "phone_home_button_hover"
                action [Hide("message_reply"), Show("phone")]
                align (0.5, 0.5)

    key [ "K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3" ]:
        action Phone.get_exit_actions()


screen phone():
    tag phone_tag
    modal True

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
                        idle app.image
                        action [Function(renpy.retain_after_load), Show(app.home_screen)]
                            
                    text app.name style "application_name" xalign 0.5

    if config_debug:
        for app in phone.applications:
            if app.notification:
                timer 0.1 action [Function(renpy.retain_after_load), Show(app.home_screen)]

        if not any(app.notification for app in phone.applications):
            timer 0.1:
                action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]