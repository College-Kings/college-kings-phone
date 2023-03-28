init python:
    class MessagerBuilder:
        def __init__(self, from_: PlayableCharacter, to: NonPlayableCharacter, clear_pending=False):
            self.from_ = from_
            self.to = to
            self.message_queue: list[Message] = []
            self.current_message: Optional[Message] = None
            self.functions = []

            if clear_pending:
                to.pending_text_messages.clear()

        def __repr__(self):
            return f"PhoneMessage(from_={self.from_}, to={self.to})"

        def new_message(self, content: str, *replies: Reply):
            self.current_message = Message(self.from_, self.to, content, replies)
            self.message_queue.append(self.current_message)

            # Moves contact to the top when receiving a new message
            try:
                messenger.contacts.insert(
                    0, messenger.contacts.pop(messenger.contacts.index(self.to))
                )
            except ValueError:
                messenger.contacts.insert(0, self.to)

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

            # Add message queue to the start of pending messages
            self.to.pending_text_messages[:0] = self.message_queue
            self.message_queue.clear()

            MessengerService.send_next_messages(self.to)


    class MessengerService:       
        @staticmethod
        def has_replies(contact: NonPlayableCharacter):
            return contact.text_messages and hasattr(contact.text_messages[-1], "replies") and contact.text_messages[-1].replies

        @staticmethod
        def send_next_messages(contact: NonPlayableCharacter):
            while contact.pending_text_messages and not MessengerService.has_replies(contact):
                contact.pending_text_messages.pop(0).send()

        @staticmethod
        def new_message(from_: PlayableCharacter, to: NonPlayableCharacter, content: str, *replies: Reply, clear_pending=True):
            to.pending_text_messages.append(Message(from_, to, content, replies))

            # Moves contact to the top when receiving a new message
            try:
                messenger.contacts.insert(
                    0, messenger.contacts.pop(messenger.contacts.index(to))
                )
            except ValueError:
                messenger.contacts.insert(0, to)

            MessengerService.send_next_messages(to)

        @staticmethod
        def add_reply(from_: PlayableCharacter, to: NonPlayableCharacter, content: str):
            MessengerService.add_replies(from_, to, Reply(content))

        @staticmethod
        def add_replies(from_: PlayableCharacter, to: NonPlayableCharacter, *replies: Reply):
            if not to.pending_text_messages or to.pending_text_messages[0].replies:
                MessengerService.new_message(from_, to, "", *replies)

            to.pending_text_messages.replies = replies