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
    def __init__(self, post: "KiwiiPost", clear_pending: bool = False) -> None:
        self.post: KiwiiPost = post
        self.clear_pending: bool = clear_pending
        self.comment_queue: list[KiwiiComment] = []
        self.current_comment: Optional[KiwiiComment] = None
        self.functions: list[
            tuple[Callable[..., Any], tuple[Any, ...], dict[str, Any]]
        ] = []

    def __repr__(self) -> str:
        return f"MessageBuilder({self.post})"

    def new_comment(
        self,
        user: ICharacter,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
        *replies: "KiwiiReply",
    ) -> "KiwiiBuilder":
        if mentions is None:
            mentions = []

        self.current_comment = KiwiiComment(
            self.post, user, message, number_likes, mentions, replies=replies
        )
        self.comment_queue.append(self.current_comment)

        return self

    def add_reply(
        self,
        message: str,
        number_likes: int = random.randint(250, 500),
        mentions: Optional[list[ICharacter]] = None,
        next_comment: Optional["KiwiiBuilder"] = None,
    ) -> "KiwiiBuilder":
        if mentions is None:
            mentions = []

        self.add_replies(KiwiiReply(message, number_likes, mentions, next_comment))

        return self

    def add_replies(
        self,
        *replies: "KiwiiReply",
    ) -> "KiwiiBuilder":
        if self.current_comment is None or self.current_comment.replies:
            return self.new_comment(self.post.user, "", 0, None, *replies)

        self.current_comment.replies = replies

        return self

    def add_function(
        self, function: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> "KiwiiBuilder":
        self.functions.append((function, args, kwargs))

        return self

    def set_variable(self, var_name: str, value: Any) -> "KiwiiBuilder":
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
