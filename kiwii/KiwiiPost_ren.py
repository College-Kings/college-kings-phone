from __future__ import annotations

import random
from typing import Callable, Optional

from game.characters.ICharacter_ren import ICharacter
from game.phone.kiwii.KiwiiComment_ren import KiwiiComment
from game.characters.PlayableCharacters_ren import mc
from game.phone.kiwii.KiwiiReply_ren import KiwiiReply

kiwii_posts: list[KiwiiPost]

"""renpy
init python:
"""


class KiwiiPost:
    def __init__(
        self,
        user: ICharacter,
        image: str,
        message: str = "",
        mentions: Optional[list[ICharacter]] = None,
        number_likes: int = random.randint(250, 500),
    ) -> None:
        self.user: ICharacter = user
        self.image: str = f"images/{image}"
        self.message: str = message
        self.mentions: list[ICharacter] = mentions if mentions is not None else []

        self.number_likes: int = number_likes

        self.liked = False
        self.seen = False

        self.sent_comments: list[KiwiiComment] = []
        self.pending_comments: list[KiwiiComment] = []

        kiwii_posts.append(self)

    @property
    def username(self) -> str:
        return self.user.username

    @property
    def profile_picture(self) -> str:
        return self.user.profile_picture

    @property
    def replies(self) -> list[KiwiiReply]:
        try:
            return self.sent_comments[-1].replies
        except (AttributeError, IndexError):
            return []

    def new_comment(
        self,
        user: ICharacter,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
    ) -> KiwiiComment:
        if mentions is None:
            mentions = []

        comment = KiwiiComment(user, message, number_likes, mentions)

        # Add message to queue
        if self.replies:
            self.pending_comments.append(comment)
        else:
            self.sent_comments.append(comment)

        self.seen = False
        return comment

    def add_reply(
        self,
        content: str,
        func: Optional[Callable[[KiwiiPost], None]] = None,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
    ) -> KiwiiReply:
        if mentions is None:
            mentions = []

        reply = KiwiiReply(content, func, number_likes, mentions)

        # Append reply to last sent message
        if self.pending_comments:
            self.pending_comments[-1].replies.append(reply)
        elif self.sent_comments:
            self.sent_comments[-1].replies.append(reply)
        else:
            message: KiwiiComment = self.new_comment(mc, "")
            message.replies.append(reply)

        return reply

    def selected_reply(self, reply: KiwiiReply) -> None:
        self.seen = True

        self.sent_comments.append(
            KiwiiComment(mc, reply.message, reply.number_likes, reply.mentions)
        )
        self.sent_comments[-1].reply = reply
        self.sent_comments[-1].replies = []

        # Run reply function
        if reply.func is not None:
            try:
                reply.func(self)
            except TypeError:
                reply.func()  # type: ignore
            reply.func = None

        # Send next queued message(s)
        try:
            while not self.replies:
                self.sent_comments.append(self.pending_comments.pop(0))
        except IndexError:
            pass

    def remove_post(self) -> None:
        if self in kiwii_posts:
            kiwii_posts.remove(self)
        del self

    # Backwards compatibility.
    def newComment(
        self,
        user: ICharacter,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
    ) -> KiwiiComment:
        if mentions is None:
            mentions = []

        return self.new_comment(user, message, number_likes, mentions)

    def addReply(
        self,
        message: str,
        func: Optional[Callable[["KiwiiPost"], None]] = None,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
    ) -> KiwiiReply:
        if mentions is None:
            mentions = []

        return self.add_reply(message, func, number_likes, mentions)

    def selectedReply(self, reply: KiwiiReply) -> None:
        return self.selected_reply(reply)
