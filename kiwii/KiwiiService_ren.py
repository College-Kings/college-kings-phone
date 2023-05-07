from typing import Union

from game.phone.kiwii.KiwiiComment_ren import KiwiiComment
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost

"""renpy
init python:
"""


class KiwiiService:
    @staticmethod
    def get_message(kiwii_obj: Union[KiwiiComment, KiwiiPost]) -> str:
        if kiwii_obj.mentions is None:
            kiwii_obj.mentions = []

        usernames: list[str] = [
            (mention.username or mention.name) for mention in kiwii_obj.mentions
        ]

        message: str = ", @".join(usernames)
        if usernames:
            message: str = (
                f"{{color=#3498DB}}{{b}}@{message}{{/b}}{{/color}} {kiwii_obj.message}"
            )
        else:
            message = kiwii_obj.message

        return message

    @staticmethod
    def toggle_liked(kiwii_obj: Union[KiwiiComment, KiwiiPost]) -> None:
        kiwii_obj.liked = not kiwii_obj.liked

        try:
            kiwii_obj.number_likes
        except AttributeError:
            # noinspection PyUnresolvedReferences
            kiwii_obj.number_likes = kiwii_obj.numberLikes

        if kiwii_obj.liked:
            kiwii_obj.number_likes += 1
        else:
            kiwii_obj.number_likes -= 1
