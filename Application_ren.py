from typing import Union

from renpy import store

from game.characters.CharacterService_ren import CharacterService
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.compat.py_compat_ren import CustomCharacter
from game.phone.messenger.MessengerService_ren import MessengerService
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiService_ren import KiwiiService
from game.phone.messenger.Reply_ren import Reply

kiwii_posts: list[KiwiiPost]

"""renpy
init python:
"""


class Application:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.home_screen: str = f"{self.name.lower()}_home"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name})"

    def __setstate__(self, state: dict[str, object]) -> None:
        if state["name"] == "Achievements":
            state["home_screen"] = "achievements_home"

        if state["name"] == "Relationships":
            state["home_screen"] = "relationships_home"

    @property
    def image(self) -> str:
        if self.notification:
            return f"{self.name.lower()}_icon_notification"
        else:
            return f"{self.name.lower()}_icon"

    @property
    def notification(self) -> bool:
        return False


class Messenger(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.contacts: list[NonPlayableCharacter] = []

    @property
    def notification(self) -> bool:
        return any(MessengerService.has_replies(contact) for contact in self.contacts)

    def __setstate__(self, state: dict[str, object]) -> None:
        image_remap = {
            "images/v10/scene 32/v9lauText.webp": "images/v0/messenger_images/v9lauText.webp",
            "images/v11/Scene 30/Laurentxtimg1.webp": "images/v0/messenger_images/Laurentxtimg1.webp",
            "images/v11/Scene 30/Laurentxtimg2.webp": "images/v0/messenger_images/Laurentxtimg2.webp",
            "images/v11/Scene 47/jennynude.webp": "images/v0/messenger_images/jennynude.webp",
            "images/v12/Scene 14/rileycatacomb.webp": "images/v0/messenger_images/rileycatacomb.webp",
            "images/v4/text1.webp": "images/v0/messenger_images/text1.webp",
            "images/v6/text2.webp": "images/v0/messenger_images/text2.webp",
            "images/v8/Scene 19/amb_pussy_pic.webp": "images/v0/messenger_images/amb_pussy_pic.webp",
            "images/v8/Scene 19/w_dick_pic.webp": "images/v0/messenger_images/w_dick_pic.webp",
            "images/v8/Scene 19/a_dick_pic.webp": "images/v0/messenger_images/a_dick_pic.webp",
            "images/v6/text3.webp": "images/v0/messenger_images/text3.webp",
            "images/v9/scene 16/v9emiKiwii.webp": "images/v0/messenger_images/v9emiKiwii.webp",
            "images/v9/Scene 35/chloetxtimg.webp": "images/v0/messenger_images/chloetxtimg.webp",
            "images/v9/Scene 35/mcdickwolves.webp": "images/v0/messenger_images/mcdickwolves.webp",
            "images/v9/Scene 35/mcdickapes.webp": "images/v0/messenger_images/mcdickapes.webp",
        }

        old_contacts = []
        if isinstance(state["contacts"], list):
            old_contacts: list[Union[NonPlayableCharacter, CustomCharacter]] = state[
                "contacts"
            ].copy()
        state["contacts"] = []

        for contact in old_contacts:
            npc = contact
            if type(npc) is not NonPlayableCharacter:
                npc = CharacterService.get_user(contact.user)  # type: ignore

            try:
                npc.text_messages
            except AttributeError:
                npc.text_messages = []

            if hasattr(contact, "sent_messages"):
                for message in contact.sent_messages:  # type: ignore
                    if hasattr(message, "message"):  # type: ignore
                        message.content = message.message  # type: ignore
                    elif hasattr(message, "image"):  # type: ignore
                        message.content = message.image  # type: ignore

                    try:
                        message.content  # type: ignore
                    except AttributeError:
                        raise AttributeError(f"{vars(message)} has no content.")

                    if message.content in image_remap:  # type: ignore
                        message.content = image_remap[message.content]  # type: ignore

                    if isinstance(message, Reply):
                        npc.text_messages.append(Reply(message.content))  # type: ignore
                    else:
                        npc.text_messages.append(Message(npc, message.content))  # type: ignore
            state["contacts"].append(npc)

        old_contacts = state["contacts"].copy()
        state["contacts"] = [
            getattr(store, contact.name.lower().replace(" ", "_"))  # type: ignore
            for contact in old_contacts  # type: ignore
        ]

        state["name"] = "Messenger"
        state["home_screen"] = "messenger_home"

        for contact in state["contacts"]:
            try:
                contact.user = CharacterService.get_user(contact.name)
            except AttributeError:
                pass

    def move_contact_to_top(self, contact: NonPlayableCharacter) -> None:
        try:
            self.contacts.insert(0, self.contacts.pop(self.contacts.index(contact)))
        except ValueError:
            self.contacts.insert(0, contact)


class Simplr(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.pending_contacts: list[NonPlayableCharacter] = []


class Kiwii(Application):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

        self.posts: list[KiwiiPost] = []

    @property
    def notification(self) -> bool:
        return any(KiwiiService.has_replies(post) for post in self.posts)

    def __setstate__(self, state: dict[str, object]) -> None:
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
            "images/phone/kiwii/Posts/v11/v11s2_nora_kiwii.webp": "images/v0/kiwii_posts/v11s2_nora_kiwii.webp",
            "images/phone/kiwii/Posts/v11/v11s38_amber_kiwii.webp": "images/v0/kiwii_posts/v11s38_amber_kiwii.webp",
            "images/phone/kiwii/posts/v11/v11s38_amber_kiwii.webp": "images/v0/kiwii_posts/v11s38_amber_kiwii.webp",
            "images/phone/kiwii/Posts/v11/v11_autumn_kiwii.webp": "images/v0/kiwii_posts/v11_autumn_kiwii.webp",
            "images/phone/kiwii/Posts/v11/v11_caleb.webp": "images/v0/kiwii_posts/v11_caleb.webp",
            "images/phone/kiwii/Posts/v11/v11_chloemcselfie.webp": "images/v0/kiwii_posts/v11_chloemcselfie.webp",
            "images/phone/kiwii/Posts/v11/v11_imrebunny.webp": "images/v0/kiwii_posts/v11_imrebunny.webp",
            "images/phone/kiwii/Posts/v11/v11_rileymcselfie.webp": "images/v0/kiwii_posts/v11_rileymcselfie.webp",
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

        if "posts" not in state:
            state["posts"] = []

        if hasattr(store, "kiwii_posts"):
            for post in kiwii_posts:
                if post.image in image_remap:
                    post.image = image_remap[post.image]

                kiwii_post = KiwiiService.new_post(
                    CharacterService.get_user(post.user),
                    post.image,
                    post.message,
                    post.number_likes,
                    post.mentions,
                )

                for comment in post.sent_comments:  # type: ignore
                    if hasattr(comment, "content"):  # type: ignore
                        comment.message = comment.content  # type: ignore

                    KiwiiService.new_comment(
                        kiwii_post,
                        CharacterService.get_user(comment.user),  # type: ignore
                        comment.message,  # type: ignore
                        comment.number_likes,  # type: ignore
                        comment.mentions,  # type: ignore
                    )

        if isinstance(state["posts"], list):
            posts: list[KiwiiPost] = state["posts"]
            for post in posts:
                if post.image in image_remap:
                    post.image = image_remap[post.image]


messenger: Messenger
achievement_app: Application
relationship_app: Application
kiwii: Kiwii
reputation_app: Application
tracker: Application
calendar: Application
