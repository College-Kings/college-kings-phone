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

            messenger.move_contact_to_top(contact)

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
        def new_message(contact: NonPlayableCharacter, content: str, *replies: Reply, clear_pending=True):
            contact.pending_text_messages.append(Message(contact, content, replies))

            messenger.move_contact_to_top(contact)

            MessengerService.send_next_messages(contact)

        @staticmethod
        def add_reply(contact: NonPlayableCharacter, content: str):
            MessengerService.add_replies(contact, Reply(content))

        @staticmethod
        def add_replies(contact: NonPlayableCharacter, *replies: Reply):
            if not contact.pending_text_messages or contact.pending_text_messages[0].replies:
                return MessengerService.new_message(contact, "", *replies)

            contact.pending_text_messages.replies = replies