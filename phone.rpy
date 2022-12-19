init python:
    class Phone:
        def __init__(self):
            self.base_image = "images/phone/phone-icon.webp"

            self.applications: list[Application] = []

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
            
            if renpy.get_screen("free_roam"):
                action Show("phone")
            else:
                action Call("call_screen_phone")

            xalign 1.0
            offset (25, -25)

label call_screen_phone:
    call screen phone
    return


screen base_phone(background="images/phone/phone_screen.webp"):
    modal True

    if len(renpy.game.context().return_stack) >= 1:
        python:
            previous_call_location = renpy.game.context().return_stack[-1][0]
            if len(previous_call_location.split("/")) == 3:
                scene_number = previous_call_location.split("/")[2].replace("scene", "").replace(".rpy", "").strip()

    add "darker_80"

    # Click background to close phone
    button:
        if (len(renpy.game.context().return_stack) >= 1
            and len(previous_call_location.split("/")) == 3
            and not renpy.has_label("{}s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("v3_1s{}".format(scene_number))):
            action Jump("v1_start")

        elif renpy.get_screen("free_roam"):
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]
        else:
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag"), Return()]

    textbutton _("Exit Phone"):
        style "phonebutton"
        if (len(renpy.game.context().return_stack) >= 1
            and len(previous_call_location.split("/")) == 3
            and not renpy.has_label("{}s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("v3_1s{}".format(scene_number))):
            action Jump("v1_start")

        elif renpy.get_screen("free_roam"):
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]
        else:
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag"), Return()]

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
        if (len(renpy.game.context().return_stack) >= 1
            and len(previous_call_location.split("/")) == 3
            and not renpy.has_label("{}s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("v3_1s{}".format(scene_number))):
            action Jump("v1_start")

        elif renpy.get_screen("free_roam"):
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]
        else:
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag"), Return()]


screen base_phone_rotated():
    modal True

    if len(renpy.game.context().return_stack) >= 1:
        python:
            previous_call_location = renpy.game.context().return_stack[-1][0]
            if len(previous_call_location.split("/")) == 3:
                scene_number = previous_call_location.split("/")[2].replace("scene", "").replace(".rpy", "").strip()

    add "darker_80"

    # Click background to close phone
    button:
        if renpy.get_screen("free_roam"):
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]
        else:
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag"), Return()]

    textbutton _("Exit Phone"):
        style "phonebutton"
        if renpy.get_screen("free_roam"):
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]
        else:
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag"), Return()]

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
        if (len(renpy.game.context().return_stack) >= 1
            and len(previous_call_location.split("/")) == 3
            and not renpy.has_label("{}s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("{}_s0{}".format(previous_call_location.split("/")[1], scene_number))
            and not renpy.has_label("v3_1s{}".format(scene_number))):
            action Jump("v1_start")

        elif renpy.get_screen("free_roam"):
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag")]
        else:
            action [Hide("tutorial"), Hide("message_reply"), Hide("phone_tag"), Return()]


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
                if renpy.get_screen("free_roam"):
                    action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
                else:
                    action [Hide("tutorial"), Hide("message_reply"), Return()]
