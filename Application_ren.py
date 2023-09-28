from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiService_ren import KiwiiService

"""renpy
init python:
"""


class Application:
    def __init__(self, name: str) -> None:
        self.name: str = name

    @property
    def home_screen(self) -> str:
        return f"{self.name.lower()}_home"

    @property
    def image(self) -> str:
        if self.notification:
            return f"{self.name.lower()}_icon_notification"
        else:
            return f"{self.name.lower()}_icon"

    @property
    def notification(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name})"


class Simplr(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.pending_contacts: list[NonPlayableCharacter] = []


class Kiwii(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self._posts: list[KiwiiPost] = []

    @property
    def posts(self) -> list[KiwiiPost]:
        try:
            self._posts
        except AttributeError:
            old_posts = self.__dict__.get("posts", [])
            self._posts = [i for i in old_posts]

        image_remap = {
            "images/phone/kiwii/Posts/v7/aupost1.webp": "images/v0/kiwii_posts/aupost1.webp",
            "images/phone/kiwii/Posts/v7/chpost1.webp": "images/v0/kiwii_posts/chpost1.webp",
            "images/phone/kiwii/Posts/v7/clpost1.webp": "images/v0/kiwii_posts/clpost1.webp",
            "images/phone/kiwii/Posts/v7/empost1.webp": "images/v0/kiwii_posts/empost1.webp",
            "images/phone/kiwii/Posts/v7/lapost1.webp": "images/v0/kiwii_posts/lapost1.webp",
            "images/phone/kiwii/Posts/v8/chlaubpost1.webp": "images/v0/kiwii_posts/chlaubpost1.webp",
            "images/phone/kiwii/Posts/v8/grpost1.webp": "images/v0/kiwii_posts/grpost1.webp",
            "images/phone/kiwii/Posts/v8/laurosepost1.webp": "images/v0/kiwii_posts/laurosepost1.webp",
            "images/phone/kiwii/Posts/v8/mcpost1a.webp": "images/v0/kiwii_posts/mcpost1a.webp",
            "images/phone/kiwii/Posts/v8/mcpost1w.webp": "images/v0/kiwii_posts/mcpost1w.webp",
            "images/phone/kiwii/Posts/v8/red_square.webp": "images/v0/kiwii_posts/red_square.webp",
            "images/phone/kiwii/Posts/v8/riclothpost1.webp": "images/v0/kiwii_posts/riclothpost1.webp",
            "images/v9/Scene 20/s20KiwiiApe.webp": "images/v0/kiwii_posts/s20KiwiiApe.webp",
            "images/v9/Scene 20/s20KiwiiWolf.webp": "images/v0/kiwii_posts/s20KiwiiWolf.webp",
            "images/phone/kiwii/Posts/v9/s20KiwiiApe.webp": "images/v0/kiwii_posts/s20KiwiiApe.webp",
            "images/phone/kiwii/Posts/v9/s20KiwiiWolf.webp": "images/v0/kiwii_posts/s20KiwiiWolf.webp",
            "images/phone/kiwii/Posts/v9/v9hlw20.webp": "images/v0/kiwii_posts/v9hlw20.webp",
            "images/v9/Scene 12/v9hlw8c.webp": "images/v0/kiwii_posts/v9hlw8c.webp",
            "images/phone/kiwii/Posts/v9/v9hlw8c.webp": "images/v0/kiwii_posts/v9hlw8c.webp",
            "images/phone/kiwii/Posts/v11/sebnaked.webp": "images/v0/kiwii_posts/sebnaked.webp",
            "images/phone/kiwii/posts/v11/sebnaked.webp": "images/v0/kiwii_posts/sebnaked.webp",
            "images/phone/kiwii/Posts/v11/v11s2_nora_kiwii.webp": "images/v0/kiwii_posts/v11s2_nora_kiwii.webp",
            "images/phone/kiwii/posts/v11/v11s2_nora_kiwii.webp": "images/v0/kiwii_posts/v11s2_nora_kiwii.webp",
            "images/phone/kiwii/Posts/v11/v11s38_amber_kiwii.webp": "images/v0/kiwii_posts/v11s38_amber_kiwii.webp",
            "images/phone/kiwii/posts/v11/v11s38_amber_kiwii.webp": "images/v0/kiwii_posts/v11s38_amber_kiwii.webp",
            "images/phone/kiwii/Posts/v11/v11_autumn_kiwii.webp": "images/v0/kiwii_posts/v11_autumn_kiwii.webp",
            "images/phone/kiwii/posts/v11/v11_autumn_kiwii.webp": "images/v0/kiwii_posts/v11_autumn_kiwii.webp",
            "images/phone/kiwii/Posts/v11/v11_caleb.webp": "images/v0/kiwii_posts/v11_caleb.webp",
            "images/phone/kiwii/posts/v11/v11_caleb.webp": "images/v0/kiwii_posts/v11_caleb.webp",
            "images/phone/kiwii/Posts/v11/v11_chloemcselfie.webp": "images/v0/kiwii_posts/v11_chloemcselfie.webp",
            "images/phone/kiwii/posts/v11/v11_chloemcselfie.webp": "images/v0/kiwii_posts/v11_chloemcselfie.webp",
            "images/phone/kiwii/Posts/v11/v11_imrebunny.webp": "images/v0/kiwii_posts/v11_imrebunny.webp",
            "images/phone/kiwii/posts/v11/v11_imrebunny.webp": "images/v0/kiwii_posts/v11_imrebunny.webp",
            "images/phone/kiwii/Posts/v11/v11_rileymcselfie.webp": "images/v0/kiwii_posts/v11_rileymcselfie.webp",
            "images/phone/kiwii/posts/v11/v11_rileymcselfie.webp": "images/v0/kiwii_posts/v11_rileymcselfie.webp",
            "images/phone/kiwii/Posts/v12/amber_bet.webp": "images/v0/kiwii_posts/amber_bet.webp",
            "images/phone/kiwii/Posts/v12/impost1.webp": "images/v0/kiwii_posts/impost1.webp",
            "images/phone/kiwii/Posts/v12/imre_raccoon.webp": "images/v0/kiwii_posts/imre_raccoon.webp",
            "images/phone/kiwii/Posts/v12/lews_post1.webp": "images/v0/kiwii_posts/lews_post1.webp",
            "images/phone/kiwii/Posts/v12/lews_post2.webp": "images/v0/kiwii_posts/lews_post2.webp",
            "images/phone/kiwii/Posts/v12/lews_post3.webp": "images/v0/kiwii_posts/lews_post3.webp",
            "images/phone/kiwii/Posts/v12/lindsey_aubrey_pjs.webp": "images/v0/kiwii_posts/lindsey_aubrey_pjs.webp",
            "images/phone/kiwii/Posts/v12/mc_bet.webp": "images/v0/kiwii_posts/mc_bet.webp",
            "images/phone/kiwii/Posts/v12/roastedape.webp": "images/v0/kiwii_posts/roastedape.webp",
            "images/phone/kiwii/Posts/v12/v12s32_15g.webp": "images/v0/kiwii_posts/v12s32_15g.webp",
            "images/phone/kiwii/Posts/v12/v12s32_24.webp": "images/v0/kiwii_posts/v12s32_24.webp",
            "images/phone/kiwii/Posts/v12/v12s32_33.webp": "images/v0/kiwii_posts/v12s32_33.webp",
            "images/phone/kiwii/Posts/v13/aubrey_beach.webp": "images/v0/kiwii_posts/aubrey_beach.webp",
        }

        for post in self._posts:
            if post.image in image_remap:
                post.image = image_remap[post.image]

        return self._posts

    @posts.setter
    def posts(self, value: list[KiwiiPost]):
        self._posts = value

    @property
    def notification(self) -> bool:
        return any(KiwiiService.has_replies(post) for post in self.posts)
