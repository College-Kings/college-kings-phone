screen reputation_home():
    tag phone_tag
    modal True

    default image_path = "images/phone/reputation/app-assets/"

    default kct_info = [
        {
            "title": _("Popular"),
            "text": _("Popular individuals are loved by the crowd and are often considered for important decisions. They prioritize their image and status over helping others."),
            "text_color": "#1C69B9"
        },
        {
            "title": _("Loyal"),
            "text": _("Loyal individuals care about other people and gain trust easily. They are known to be responsible, but can be a bit of a buzzkill when it comes to doing crazy stuff."),
            "text_color": "#DC9D05"
        },
        {
            "title": _("Confident"),
            "text": _("Confident individuals don't rely on others to join them in their actions. They don't crave their friends' approval, however they can be perceived as egotistical."),
            "text_color": "#be66a8"
        }
    ]
    default kct_info_index = 0

    use base_phone(image_path + "kct-background.webp"):
        fixed:
            pos (12, 6)
            ysize 128

            imagebutton:
                idle "back_button"
                action Show("phone")
                xpos 20
                yalign 0.75

        vbox:
            align (0.5, 0.5)
            spacing 20
            
            for count, rep in enumerate(reputation.sorted_reputations, start=1):
                frame:
                    if count == 1:
                        background image_path + "kct-{}.webp".format(rep.name.lower())
                    else:
                        background image_path + "kct-disabled.webp"
                    xysize (320, 79)

                    text _("[count]. [rep.name]"):
                        align (0.5, 0.5)

                        if count == 1:
                            color "#fff"
                        elif rep == Reputations.CONFIDENT:
                            color "#be66a8"
                        elif rep == Reputations.LOYAL:    
                            color "#DC9D05"
                        elif rep == Reputations.POPULAR:
                            color "#1C69B9"

    # KCT Tutorial
    frame:
        background image_path + "kct-box-background.webp"
        xpos 1280
        yalign 0.5
        xysize (535, 330)

        fixed:
            ysize 28
            ypos 6

            text kct_info[kct_info_index]["title"].upper():
                style "kct_info_title"
                align (0.5, 0.5)

        fixed:
            ysize 281
            ypos 42

            imagebutton:
                idle "tutorial_left_button_idle"
                hover "tutorial_left_button_hover"
                action SetLocalVariable("kct_info_index", max(0, kct_info_index - 1))
                yalign 0.5

            text kct_info[kct_info_index]["text"]:
                style "kct_info_text"
                xsize 400
                align (0.5, 0.5)

            imagebutton:
                idle "tutorial_right_button_idle"
                hover "tutorial_right_button_hover"
                action SetLocalVariable("kct_info_index", min(kct_info_index + 1, len(kct_info) - 1))
                align (1.0, 0.5)

    use kct_points


screen kct_points():
    style_prefix "kct_points"

    default bro = reputation.components[RepComponent.BRO]
    default boyfriend = reputation.components[RepComponent.BOYFRIEND]
    default troublemaker = reputation.components[RepComponent.TROUBLEMAKER]

    frame:
        background "images/phone/reputation/app-assets/kct-diagram.webp"
        xysize (506, 424)
        xpos 120
        yalign 0.5
        
        frame:
            xysize (40, 40)
            pos (233, 15)

            text _("[bro]") align (0.5, 0.5)
        
        frame:
            xysize (35, 35)
            pos (25, 354)

            text _("[boyfriend]") align (0.5, 0.5)

        frame:
            xysize (35, 35)
            pos (446, 354)

            text _("[troublemaker]") align (0.5, 0.5)


style kct_info_title is text:
    font "fonts/Syne-ExtraBold.ttf"
    size 19
    color "#ffffff"

style kct_info_text is text:
    font "fonts/Effra-Regular.ttf"
    size 23
    color "#fff"
    text_align 0.5
    