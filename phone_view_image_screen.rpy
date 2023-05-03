screen phone_view_image(image_path=None):
    modal True

    $ bigImage = os.path.splitext(image_path)[0] + "big" + os.path.splitext(image_path)[1]

    add "darker_80"
    if renpy.loadable(bigImage):
        add bigImage at truecenter
    else:
        add img at truecenter

    button:
        action Hide("phone_image")