init python:
    class Phone:
        def __init__(self):
            self.base_image = "images/phone/phone-icon.webp"

            self.applications: list[Application] = [messenger, achievement_app, relationship_app, kiwii, reputation_app, tracker, calendar]

        @property
        def notification(self):
            return any(app.notification for app in self.applications)

        @property
        def image(self):
            if not self.notification:
                return self.base_image

            file_name, extension = os.path.splitext(self.base_image)
            return file_name + "-notification" + extension


default phone = Phone()


screen phone_icon():
    zorder 100
    
    if not renpy.get_screen("choice") and not renpy.get_screen("censored_popup") and not renpy.get_screen("phone_tag"):
        imagebutton:
            idle phone.image
            action Show("phone")
            xalign 1.0
            offset (25, -25)


screen base_phone(background="images/phone/phone_screen.webp"):
    modal True

    add "darker_80"

    # Click background to close phone
    button:
        action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]

    textbutton _("Exit Phone"):
        style "phonebutton"
        action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]

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
                    idle "images/phone/home_button_idle.webp"
                    hover "images/phone/home_button_hover.webp"
                    action [Hide("message_reply"), Show("phone")]
                    align (0.5, 0.5)

    key [ "K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3" ]:
        action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]



screen base_phone_rotated():
    modal True

    add "darker_80"

    # Click background to close phone
    button:
        action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]

    textbutton _("Exit Phone"):
        style "phonebutton"
        action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]

    frame:
        align (0.5, 0.5)
        xysize (918, 433)
        modal True

        transclude

        fixed:
            xsize 69
            xpos 844

            imagebutton:
                if renpy.get_screen("kiwiiPost") or renpy.get_screen("kiwiiApp") or renpy.get_screen("kiwiiPreferences"):
                    idle "images/phone/home_button_kiwii_idle.webp"
                    hover "images/phone/home_button_kiwii_hover.webp"
                else:
                    idle "images/phone/home_button_idle.webp"
                    hover "images/phone/home_button_hover.webp"
                action [Hide("message_reply"), Show("phone")]
                align (0.5, 0.5)

    key [ "K_ESCAPE", "K_MENU", "K_PAUSE", "mouseup_3" ]:
        action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]


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
