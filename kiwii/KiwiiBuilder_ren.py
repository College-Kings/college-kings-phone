from __future__ import annotations
import random
from typing import Any, Callable, Optional

from game.characters.ICharacter_ren import ICharacter
from game.phone.kiwii.KiwiiComment_ren import KiwiiComment
from game.phone.kiwii.KiwiiPost_ren import KiwiiPost
from game.phone.kiwii.KiwiiReply_ren import KiwiiReply
from game.phone.kiwii.KiwiiService_ren import KiwiiService

SetVariable: Any

"""renpy
init python:
"""


class KiwiiBuilder:
    def __init__(self, post: KiwiiPost, clear_pending: bool = False) -> None:
        self.post: KiwiiPost = post
        self.clear_pending: bool = clear_pending
        self.comment_queue: list[KiwiiComment] = []
        self.current_comment: Optional[KiwiiComment] = None
        self.functions: list[tuple[Callable[..., Any], tuple[Any], dict[str, Any]]] = []

    def __repr__(self) -> str:
        return f"MessageBuilder({self.post})"

    def new_comment(
        self,
        post: KiwiiPost,
        user: ICharacter,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
        *replies: KiwiiReply,
    ) -> KiwiiBuilder:
        if mentions is None:
            mentions = []

        post.pending_comments.append(
            KiwiiComment(post, user, message, mentions, number_likes, replies=replies)
        )

        KiwiiService.send_next_comments(post)

        return self

    def add_reply(
        self,
        post: KiwiiPost,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
        next_message: Optional[KiwiiBuilder] = None,
    ) -> KiwiiBuilder:
        if mentions is None:
            mentions = []

        KiwiiService.add_replies(
            post, KiwiiReply(message, number_likes, mentions, next_message)
        )

        return self

    def add_replies(
        self,
        post: KiwiiPost,
        *replies: KiwiiReply,
    ) -> KiwiiBuilder:
        if not post.pending_comments or post.pending_comments[0].replies:
            KiwiiService.new_comment(post, post.user, "", 0, None, *replies)

        post.pending_comments[-1].replies = replies

        return self

    def add_function(
        self, function: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> KiwiiBuilder:
        self.functions.append((function, args, kwargs))

        return self

    def set_variable(self, var_name: str, value: Any) -> KiwiiBuilder:
        self.add_function(SetVariable(var_name, value))

        return self

    def send(self) -> None:
        for function, args, kwargs in self.functions:
            function(*args, **kwargs)

        if self.clear_pending:
            self.post.pending_comments.clear()

        # Add message queue to the start of pending messages
        self.post.pending_comments[:0] = self.comment_queue
        self.comment_queue.clear()

        KiwiiService.send_next_comments(self.post)
