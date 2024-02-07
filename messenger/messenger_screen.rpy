screen messenger(contact=None):
    tag phone_tag
    modal True

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
                                if isinstance(message, Reply):
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

            vbox:
                xsize 500
                xpos 450
                yalign 1.0
                yoffset -100
                spacing 10

                for reply in MessengerService.replies(contact):
                    button:
                        if reply.next_message is not None:
                            action [AddToSet(contact.text_messages, reply), Function(reply.next_message.send)]
                        else:
                            action [AddToSet(contact.text_messages, reply), Function(MessengerService.send_next_messages, contact)]
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

    if config_debug:
        $ replies = MessengerService.replies(contact)
        if replies:
            $ reply = renpy.random.choice(replies)
            timer 0.1 repeat True:
                if reply.next_message is not None:
                    action [AddToSet(contact.text_messages, reply), Function(reply.next_message.send)]
                else:
                    action [AddToSet(contact.text_messages, reply), Function(MessengerService.send_next_messages, contact)]
        else:
            timer 0.1 action Phone.get_exit_actions()