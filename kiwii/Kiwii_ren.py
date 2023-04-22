"""renpy
init python:
"""

from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from renpy.exports import store

    from game.phone.kiwii.KiwiiPost_ren import KiwiiPost


def get_total_likes() -> int:
    return sum(
        post.number_likes for post in store.kiwii_posts if post.user == store.mc
    ) + sum(
        comment.number_likes
        for post in store.kiwii_posts
        for comment in post.sent_comments
        if comment.user == store.mc
    )


def find_kiwii_post(
    image: Optional[str] = None, message: Optional[str] = None
) -> KiwiiPost:
    for post in store.kiwii_posts:
        if post.image == image:
            return post
        if post.message == message:
            return post
