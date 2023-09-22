screen achievements_home():
    tag phone_tag
    modal True
    
    use base_phone:
        frame:
            background "achievements_background"

            viewport:
                ysize 710
                ypos 134
                mousewheel True
                draggable True

                vbox:
                    xalign 0.5
                    spacing -40

                    for ach in Achievement.all_achievements:
                        frame:
                            xsize 415
                            ypadding 35
                            xalign 0.5

                            if achievement.has(ach.id):
                                background "achievements_unlocked"

                                vbox:
                                    xsize 320
                                    pos (50, -2)

                                    text ach.display_name.upper() style "achievement_name"
                                    text ach.description style "achievement_text"
                                
                            else:
                                background "achievements_locked"

                                text ach.display_name.upper() style "achievement_locked_name" xsize 320 pos (50, -2)
