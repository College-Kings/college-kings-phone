from typing import Any, Callable, Optional

from renpy import store
from renpy.exports import SetVariable

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.phone.Message_ren import Message
from game.phone.MessengerService_ren import MessengerService
from game.phone.Reply_ren import Reply


"""renpy
init python:
"""


class MessageBuilder:
    def __init__(self, contact: NonPlayableCharacter, clear_pending=False) -> None:
        self.contact: NonPlayableCharacter = contact
        self.clear_pending: bool = clear_pending
        self.message_queue: list[Message] = []
        self.current_message: Optional[Message] = None
        self.functions: list[Callable] = []

    def __repr__(self) -> str:
        return f"MessageBuilder({self.contact})"

    def new_message(self, content: str, *replies: Reply) -> None:
        self.current_message = Message(self.contact, content, replies)
        self.message_queue.append(self.current_message)

        store.messenger.move_contact_to_top(self.contact)

        return self

    def add_reply(self, content: str, next_message=None) -> None:
        self.add_replies(Reply(content, next_message))

        return self

    def add_replies(self, *replies: Reply) -> None:
        if self.current_message is None or self.current_message.replies:
            return self.new_message("", *replies)

        self.current_message.replies = replies

        return self

    def add_function(self, function: Callable, *args, **kwargs) -> None:
        self.functions.append((function, args, kwargs))

        return self

    def set_variable(self, var_name: str, value: Any) -> None:
        self.add_function(SetVariable(var_name, value))

        return self

    def send(self) -> None:
        for function, args, kwargs in self.functions:
            function(*args, **kwargs)

        if self.clear_pending:
            self.contact.pending_text_messages.clear()

        # Add message queue to the start of pending messages
        self.contact.pending_text_messages[:0] = self.message_queue
        self.message_queue.clear()

        MessengerService.send_next_messages(self.contact)
