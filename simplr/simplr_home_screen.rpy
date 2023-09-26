screen simplr_home():
    tag phone_tag
    modal True

    python:
        try:
            simplr_contact = simplr_app.pending_contacts[0]
        except IndexError:
            simplr_contact = None

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
                    background [p for p in simplr_contact.profile_pictures if p.endswith("simplr.webp")][0]
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
                            action [AddToSet(messenger.contacts, simplr_contact), RemoveFromSet(simplr_app.pending_contacts, simplr_contact)]

                        imagebutton:
                            idle "simplr_no_button_idle"
                            hover "simplr_no_button_hover"
                            action RemoveFromSet(simplr_app.pending_contacts, simplr_contact)

            else:
                text _("No new profiles to show...\nYou can however still chat with your matches!\n\nBe sure to check back soon!"):
                    style "simplr_no_more_profiles"
                    align (0.5, 0.5)
                    xsize 340
