screen messenger(contact=None):
    tag phone_tag
    modal True
    predict False

    use base_phone:
        frame:
            background "messenger_conversation_background"
            xysize (433, 918)

            hbox:
                pos (41, 62)
                ysize 93
                spacing 15

                imagebutton:
                    idle "phone_back_button"
                    action Show("messenger_home")
                    yalign 0.5

                add Transform(contact.profile_picture, xysize=(65, 65)) yalign 0.5

                text contact.name style "nametext" yalign 0.5

            viewport:
                id "messenger_vp"
                mousewheel True
                draggable True
                pos (11, 157)
                xysize (416, 686)

                vbox:
                    xfill True

                    null height 25

                    for message in contact.text_messages:
                        if message.content.strip():
                            frame:
                                if isinstance(message, Reply) or isinstance(message.contact, PlayableCharacter):
                                    background "phone_reply_background"
                                    xalign 1.0

                                    if renpy.loadable(message.content):
                                        padding (25, 25)

                                        imagebutton:
                                            idle Transform(message.content, zoom=0.15)
                                            action Show("phone_image", img=message.content)
                                    else:
                                        padding (40, 30)

                                        text message.content  style "reply_text"

                                else:
                                    background "phone_message_background"

                                    if renpy.loadable(message.content):
                                        padding (25, 25)

                                        imagebutton:
                                            idle Transform(message.content, zoom=0.15)
                                            action Show("phone_image", img=message.content)
                                    else:
                                        padding (40, 30)

                                        text message.content  style "message_text"

                    null height 75

            $ replies = MessengerService.replies(contact)

            vbox:
                xsize 500
                xpos 450
                yalign 1.0
                yoffset -100
                spacing 10

                for index, reply in enumerate(replies):
                    button:
                        action SendReply(contact, index)
                        sensitive True
                        padding (15, 15)
                        size_group "reply_buttons"

                        if renpy.loadable(reply.content):
                            add Transform(reply.content, zoom=0.15)
                        else:
                            background "phone_reply_background_idle"
                            text reply.content style "reply_text" align (0.5, 0.5)

    $ messenger_vp = renpy.get_displayable(None, "messenger_vp")
    $ messenger_vp.yoffset = 1.0

    if not replies:
        on "hide" action Function(messenger.remove_notification, contact)
        on "replaced" action Function(messenger.remove_notification, contact)


    if config_debug:
        if replies:
            $ index = random.randint(0, len(replies) - 1)
            timer 0.1 repeat True action SendReply(contact, index)
        
        else:
            timer 0.1 repeat True action Phone.get_exit_actions()
