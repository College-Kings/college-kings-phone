screen kiwii_base():
    modal True

    use base_phone:
        frame:
            background "kiwii_background"

            transclude

            hbox:
                ysize 72
                xalign 0.5
                ypos 843
                spacing 45

                imagebutton:
                    idle "kiwii_home_button_idle"
                    hover "kiwii_home_button_hover"
                    action Show("kiwii_home")
                    yalign 0.5

                null width 25

                null width 45

                imagebutton:
                    idle "kiwii_liked_button_idle"
                    hover "kiwii_liked_button_hover"
                    action Show("kiwii_home", posts=list(filter(lambda post: post.liked, kiwii_posts)))
                    yalign 0.5

                imagebutton:
                    idle Transform(mc.profile_picture, xysize=(30, 30))
                    action Show("kiwii_preferences")
                    yalign 0.5


screen kiwii_preferences():
    tag phone_tag
    modal True

    default profile_pictures_index = 0
    $ mc.profile_picture = mc.profile_pictures[profile_pictures_index]

    use kiwii_base:
        vbox:
            xalign 0.5
            ypos 175
            spacing 25

            vbox:
                xalign 0.5
                spacing 5

                add Transform(mc.profile_picture, xysize=(200, 200)) xalign 0.5

                hbox:
                    spacing 50
                    xalign 0.5

                    textbutton "<":
                        if profile_pictures_index > 0:
                            action SetScreenVariable("profile_pictures_index", profile_pictures_index - 1)
                        text_style "kiwii_PrefTextButton"

                    textbutton ">":
                        if profile_pictures_index + 1 < len(mc.profile_pictures):
                            action SetScreenVariable("profile_pictures_index", profile_pictures_index + 1)
                        text_style "kiwii_PrefTextButton"

            vbox:
                xalign 0.5

                text "Username:" style "kiwii_ProfileName" xalign 0.5
                input:
                    value FieldInputValue(mc, "username")
                    default mc.username
                    length 15
                    color "#006400"
                    outlines [ (absolute(0), "#000", absolute(0), absolute(0)) ]
                    xalign 0.5

            vbox:
                xalign 0.5

                text "Total Likes:" style "kiwii_ProfileName" at truecenter
                text str(get_total_likes()) at truecenter:
                    color "#006400"
                    outlines [ (absolute(0), "#000", absolute(0), absolute(0)) ]


screen kiwii_home(posts=kiwii_posts):
    tag phone_tag
    modal True

    use kiwii_base:

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

                                add Transform(post.profile_picture, xysize=(55, 55))
                                text post.username style "kiwii_ProfileName" yalign 0.5

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

    if config_debug:
        for post in reversed(posts):
            if post.replies:
                timer 0.1 action Show("kiwiiPost", post=post)
        
        if not any(post.replies for post in reversed(posts)):
            timer 0.1:
                if renpy.get_screen("free_roam"):
                    action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
                else:
                    action [Hide("tutorial"), Hide("message_reply"), Return()]


screen kiwiiPost(post):
    tag phone_tag
    zorder 200
    modal True

    $ post.seen = True

    use kiwii_base:
        imagebutton:
            idle Transform(post.image, xysize=(416, 234))
            action Show("kiwii_image", img=post.image)
            xalign 0.5
            ypos 152
            
        viewport:
            mousewheel True
            draggable True
            xysize (357, 400)
            pos (20, 386)

            vbox:
                spacing 20

                null

                for comment in post.sent_comments:
                    if comment.message.strip():
                        vbox:
                            spacing 5

                            hbox:
                                spacing 10

                                add Transform(comment.user.profile_picture, xysize=(55, 55))
                                text str(comment.user.username or comment.user.name) style "kiwii_ProfileName" yalign 0.5

                            text KiwiiService.get_message(comment) style "kiwii_CommentText"

                            hbox:
                                spacing 5

                                imagebutton:
                                    idle "kiwii_like_idle"
                                    hover "kiwii_like_hover"
                                    selected_idle "kiwii_like_hover"
                                    selected comment.liked
                                    action Function(KiwiiService.toggle_liked, comment)
                                text "[comment.number_likes]" style "kiwii_LikeCounter" yalign 0.5

    if post.replies:
        vbox:
            xpos 1200
            yalign 0.84
            spacing 15

            for reply in post.replies:
                textbutton reply.message:
                    text_style "kiwii_ReplyText"
                    style "kiwii_reply"
                    action Function(post.selectedReply, reply)

    if config_debug:
        if post.replies:
            $ reply = renpy.random.choice(post.replies)
            timer 0.1 repeat True action Function(post.selectedReply, reply)
        else:
            timer 0.1:
                if renpy.get_screen("free_roam"):
                    action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
                else:
                    action [Hide("tutorial"), Hide("message_reply"), Return()]


screen kiwii_image(img):
    zorder 100
    modal True

    imagebutton:
        idle Transform(img, zoom=0.85)
        action Hide("kiwii_image")
        align (0.5, 0.5)