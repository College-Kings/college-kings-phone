from typing import Optional

from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.characters.PlayableCharacters_ren import mc

kiwii_posts: list[KiwiiPost]

"""renpy
init python:
"""


def get_total_likes() -> int:
    return sum(post.number_likes for post in kiwii_posts if post.user == mc) + sum(
        comment.number_likes
        for post in kiwii_posts
        for comment in post.sent_comments
        if comment.user == mc
    )


def find_kiwii_post(
    image: Optional[str] = None, message: Optional[str] = None
) -> Optional[KiwiiPost]:
    for post in kiwii_posts:
        if post.image == image:
            return post
        if post.message == message:
            return post
