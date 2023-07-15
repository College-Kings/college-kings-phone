screen kiwii_fan_page(posts):
    tag phone_tag
    modal True

    use base_phone:
        frame:
            background "kiwii_background"

        viewport:
            mousewheel True
            draggable True
            ypos 152
            ysize 692

            vbox:
                xalign 0.5
                xsize 416

                null height 20

                for post in reversed(posts):
                    frame:
                        xalign 0.5
                        xsize 386
                        padding (10, 10)

                        has vbox

                        hbox:
                            xsize 366

                            hbox:
                                spacing 10

                                add Transform(post.user.profile_picture, xysize=(55, 55))
                                text post.user.username style "kiwii_ProfileName" yalign 0.5

                            hbox:
                                spacing 5
                                align (1.0, 0.5)

                                add "kiwii_static_button_1"
                                add "kiwii_static_button_2"

                        null height 10

                        vbox:
                            spacing 5

                            imagebutton:
                                idle Transform(post.image, xysize=(366, 206))
                                action Show("kiwii_image", img=post.image)
                                xalign 0.5
                            text KiwiiService.get_message(post) style "kiwii_CommentText" xalign 0.5

                        null height 10

                        hbox:
                            xsize 366

                            hbox:
                                imagebutton:
                                    idle "kiwii_like_idle"
                                    hover "kiwii_like_hover"
                                    selected_idle "kiwii_like_hover"
                                    selected post.liked
                                    action Function(KiwiiService.toggle_liked, post)

                                text "{}".format(post.number_likes) style "kiwii_LikeCounter" yalign 0.5

                            imagebutton:
                                idle "kiwii_comment_idle"
                                hover "kiwii_comment_hover"
                                action Show("kiwiiPost", post=post)
                                xalign 1.0


            hbox:
                ysize 72
                xalign 0.5
                ypos 843
                spacing 45

                imagebutton:
                    idle "kiwii_home_button_idle"
                    hover "kiwii_home_button_hover"
                    action Hide()
                    yalign 0.5

                null width 25

                null width 45

                imagebutton:
                    idle Transform(mc.profile_picture, xysize=(30, 30))
                    action Show("kiwii_preferences")
                    yalign 0.5

    # if config_debug:
    #     for post in reversed(posts):
    #         if KiwiiService.has_replies(post):
    #             timer 0.1 action Show("kiwiiPost", post=post)
        
    #     if not any(KiwiiService.has_replies(post) for post in reversed(posts)):
    #         timer 0.1:
    #             if renpy.get_screen("free_roam"):
    #                 action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
    #             else:
    #                 action [Hide("tutorial"), Hide("message_reply"), Return()]