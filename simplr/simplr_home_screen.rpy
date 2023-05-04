screen simplr_home():
    tag phone_tag
    modal True
    
    $ simplr_contact = simplr_app.pending_contacts[0] or None

    use base_phone:
        frame:
            background "simplr_background"
            
            # Top UI
            imagebutton:
                pos (340, 100)
                idle "simplr_message_icon_idle"
                hover "simplr_message_icon_hover"
                action Show("messenger_home")

            if simplr_contact is not None:
                frame:
                    background simplr_contact.profile_picture
                    xysize (370, 593)
                    xalign 0.5
                    ypos 200
                    
                    hbox:
                        align (0.5, 1.0)
                        yoffset -10
                        spacing 10

                        imagebutton:
                            idle "simplr_like_button_idle"
                            hover "simplr_like_button_hover"
                            action AddToSet(messenger.contacts, simplr_app.pending_contacts.pop(0))

                        imagebutton:
                            idle "simplr_no_button_idle"
                            hover "simplr_no_button_hover"
                            action Function(simplr_app.pending_contacts.pop, 0)

            else:
                text _("No new profiles to show...\nYou can however still chat with your matches!\n\nBe sure to check back soon!"):
                    style "simplr_no_more_profiles"
                    align (0.5, 0.5)
                    xsize 340
