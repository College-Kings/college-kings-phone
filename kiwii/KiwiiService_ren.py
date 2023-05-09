import random
from typing import Optional, Union
from game.characters.ICharacter_ren import ICharacter

from game.phone.Application_ren import kiwii
from game.phone.kiwii.KiwiiComment_ren import KiwiiComment
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.characters.PlayableCharacters_ren import mc
from game.phone.kiwii.KiwiiReply_ren import KiwiiReply
from game.phone.kiwii.KiwiiBuilder_ren import KiwiiBuilder


"""renpy
init python:
"""


class KiwiiService:
    @staticmethod
    def has_replies(post: KiwiiPost) -> bool:
        try:
            return bool(post.comments[-1].replies)
        except (IndexError, AttributeError):
            return False

    @staticmethod
    def send_next_comments(post: KiwiiPost) -> None:
        while post.pending_comments and not KiwiiService.has_replies(post):
            post.pending_comments.pop(0).send()

    @staticmethod
    def new_post(
        user: ICharacter,
        image: str,
        message: str,
        mentions: Optional[list[ICharacter]] = None,
        number_likes: int = random.randint(250, 500),
    ) -> KiwiiPost:
        if mentions is None:
            mentions = []

        post = KiwiiPost(user, image, message, mentions, number_likes)
        kiwii.posts.append(post)

        return post

    @staticmethod
    def new_comment(
        post: KiwiiPost,
        user: ICharacter,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
        *replies: KiwiiReply,
    ) -> None:
        if mentions is None:
            mentions = []

        post.pending_comments.append(
            KiwiiComment(post, user, message, mentions, number_likes, replies=replies)
        )

        KiwiiService.send_next_comments(post)

    @staticmethod
    def add_reply(
        post: KiwiiPost,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
        next_message: Optional[KiwiiBuilder] = None,
    ) -> None:
        if mentions is None:
            mentions = []

        KiwiiService.add_replies(
            post, KiwiiReply(message, number_likes, mentions, next_message)
        )

    @staticmethod
    def add_replies(
        post: KiwiiPost,
        *replies: KiwiiReply,
    ) -> None:
        if not post.pending_comments or post.pending_comments[0].replies:
            KiwiiService.new_comment(post, post.user, "", 0, None, *replies)

        post.pending_comments[-1].replies = replies

    @staticmethod
    def get_message(kiwii_obj: Union[KiwiiPost, KiwiiComment]) -> str:
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
    def toggle_liked(kiwii_obj: Union[KiwiiPost, KiwiiComment]) -> None:
        kiwii_obj.liked = not kiwii_obj.liked

        if kiwii_obj.liked:
            kiwii_obj.number_likes += 1
        else:
            kiwii_obj.number_likes -= 1

    @staticmethod
    def delete_post(kiwii_obj: KiwiiPost) -> None:
        try:
            kiwii.posts.remove(kiwii_obj)
        except ValueError:
            pass

    @staticmethod
    def get_total_likes() -> int:
        return sum(post.number_likes for post in kiwii.posts if post.user == mc) + sum(
            comment.number_likes
            for post in kiwii.posts
            for comment in post.comments
            if comment.user == mc
        )

    @staticmethod
    def find_post(
        image: Optional[str] = None, message: Optional[str] = None
    ) -> Optional[KiwiiPost]:
        for post in kiwii.posts:
            if post.image == image:
                return post
            if post.message == message:
                return post
