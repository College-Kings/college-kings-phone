screen relationships_home():
    tag phone_tag

    default image_path = "images/phone/relationships/app-assets/"
    default girls = NonPlayableCharacter.characters.values()

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

                for girl in girls:
                    frame:
                        padding (10, 10)
                        xsize 238
                        background "relationships_frame_background"

                        hbox:
                            spacing 15

                            add Transform(girl.profile_picture, xysize=(65, 65)) yalign 0.5

                            vbox:
                                yalign 0.5

                                text girl.name

                                if girl.relationship < Relationship.FRIEND:
                                    text "Complicated":
                                        size 20
                                        color "#FFD166"

                                elif girl.relationship == Relationship.FRIEND:
                                    text "Friend":
                                        size 20
                                        color "#FFD166"
                                    
                                elif girl.relationship < Relationship.KISS:
                                    if girl == penelope: ### Penelope could be on LIKES. Which we could fix...
                                        text "Kissed":
                                            size 20
                                            color "#FFD166"
                                    else:
                                        text "Friends":
                                            size 20
                                            color "#FFD166"

                                elif girl.relationship == Relationship.KISS:
                                    text "Kissed":
                                        size 20
                                        color "#FFD166"

                                elif girl.relationship == Relationship.FWB:
                                    text "Friends with Benefits":
                                        size 20
                                        color "#FFD166"

                                elif girl.relationship < Relationship.GIRLFRIEND: # that grey area for Autumn and Amber (and maybe Penelope)
                                    text "Loyal/Trust":
                                        size 20
                                        color "#FFD166"
                                
                                elif girl.relationship == Relationship.GIRLFRIEND:
                                    text "Dating":
                                        size 20
                                        color "#FFD166"
                                
                                else: # shouldn't happen, but just a failsafe
                                    text girl.relationship.name.capitalize():

                                        size 20
                                        color "#FFD166"
