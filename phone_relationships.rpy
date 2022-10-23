screen relationships_home():
    tag phone_tag

    default image_path = "images/phone/relationships/app-assets/"

    use base_phone_rotated:
        frame:
            background image_path + "background.webp"
            
            vpgrid:
                mousewheel True
                draggable True
                cols 3
                spacing 25
                pos (85, 85)
                xysize (765, 335)
                allow_underfull True

                for character in (
                    amber,
                    aubrey,
                    autumn,
                    cameron,
                    chloe,
                    chris,
                    elijah,
                    emily,
                    emmy,
                    imre,
                    jenny,
                    josh,
                    lauren,
                    lindsey,
                    mr_lee,
                    ms_rose,
                    naomi,
                    nora,
                    penelope,
                    riley,
                    ryan,
                    samantha,
                ):
                    frame:
                        padding (10, 10)
                        xsize 238
                        background "relationships_frame_background"

                        hbox:
                            spacing 15

                            add Transform(character.profile_picture, xysize=(65, 65)) yalign 0.5

                            vbox:
                                yalign 0.5

                                text character.name

                                if character.relationship == Relationship.EX:
                                    text _("Broken Up"):
                                        size 20
                                        color "#FFD166"
                                
                                elif character.relationship == Relationship.KISS:
                                    text _("Kissed"):
                                        size 20
                                        color "#FFD166"

                                elif character.relationship == Relationship.FWB:
                                    text _("Friends with Benefits"):
                                        size 20
                                        color "#FFD166"

                                elif character.relationship == Relationship.GIRLFRIEND or character.relationship == Relationship.TAMED:
                                    text _("Dating"):
                                        size 20
                                        color "#FFD166"

                                else:
                                    text character.relationship.name.capitalize():

                                        size 20
                                        color "#FFD166"
