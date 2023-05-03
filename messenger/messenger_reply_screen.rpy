screen message_reply(contact):
    vbox:
        xsize 500
        xpos 1200
        yalign 1.0
        yoffset -100
        spacing 10

        for reply in contact.text_messages[-1].replies:
            button:
                if reply.next_message is not None:
                    action [AddToSet(contact.text_messages, reply), Function(reply.next_message.send), Hide()]
                else:
                    action [AddToSet(contact.text_messages, reply), Function(MessengerService.send_next_messages, contact), Hide()]
                sensitive True
                padding (15, 15)
                size_group "reply_buttons"

                if renpy.loadable(reply.content):
                    add Transform(reply.content, zoom=0.15)
                else:
                    background "phone_reply_background_idle"
                    text reply.content style "reply_text" align (0.5, 0.5)

    if config_debug:
        $ reply = renpy.random.choice(contact.text_messages[-1].replies)
        
        if isinstance(reply, NonPlayableCharacter):
            $ print(contact.text_messages[-1].content)
        
        timer 0.1:
            if reply.next_message is not None:
                action [AddToSet(contact.text_messages, reply), Function(reply.next_message.send), Hide()]
            else:
                action [AddToSet(contact.text_messages, reply), Function(MessengerService.send_next_messages, contact), Hide()]