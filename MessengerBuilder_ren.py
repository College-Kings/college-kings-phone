"""renpy
init python:
"""


from game.phone.MessengerService_ren import MessengerService


class MessageBuilder:
    def __init__(self, contact: NonPlayableCharacter, clear_pending=False):
        self.contact = contact
        self.clear_pending = clear_pending
        self.message_queue: list[Message] = []
        self.current_message: Optional[Message] = None
        self.functions = []

    def __repr__(self):
        return f"MessageBuilder({self.contact})"

    def new_message(self, content: str, *replies: Reply):
        self.current_message = Message(self.contact, content, replies)
        self.message_queue.append(self.current_message)

        messenger.move_contact_to_top(self.contact)

    def add_reply(self, content: str):
        self.add_replies(Reply(content))

    def add_replies(self, *replies: Reply):
        if self.current_message is None or self.current_message.replies:
            return self.new_message("", *replies)

        self.current_message.replies = replies

    def add_function(self, function: Callable, *args, **kwargs):
        self.functions.append((function, args, kwargs))

    def set_variable(self, var_name: str, value: Any):
        self.add_function(SetVariable(var_name, value))

    def send(self):
        for function, args, kwargs in self.functions:
            function(*args, **kwargs)

        if self.clear_pending:
            self.contact.pending_text_messages.clear()

        # Add message queue to the start of pending messages
        self.contact.pending_text_messages[:0] = self.message_queue
        self.message_queue.clear()

        MessengerService.send_next_messages(self.contact)
