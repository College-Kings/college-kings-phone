init python:
    class MessageList:
        def __init__(self):
            self.head: Message = None

        def insertAfter(self, prev_node: Message, new_node: Message):
            if prev_node is None:
                raise IndexError("The given previous node must be in the List.")

            new_node.next_message = prev_node.next_message
            prev_node.next_message = new_node

        def append(self, new_node: Message):
            if self.head is None:
                self.head = new_node
                return

            last = self.head
            while (last.next_message):
                last = last.next_message

            last.next = new_node

        def print_list(self):
            temp = self.head
            while (temp):
                print(temp.data)
                temp = temp.next


    class MessagerBuilder:
        def __init__(self, from_: PlayableCharacter, to: NonPlayableCharacter):
            self.from_ = from_
            self.to = to
            self.message_queue: list[Message] = []
            self.current_message: Optional[Message] = None
            self.functions = []

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

            self.notification = True

            return self

        def add_replies(self, *replies: Reply):
            if self.current_message is None or self.current_message.replies:
                return self.new_message("", *replies)

            self.current_message.replies = replies
            return self

        def add_function(self, function: Callable, *args, **kwargs):
            self.functions.append((function, args, kwargs))
            return self

        def send(self):
            for function, args, kwargs in self.functions:
                function(*args, **kwargs)

            # Add message queue to the start of pending messages
            self.to.pending_text_messages[:0] = self.message_queue

            MessengerService.send_next_messages(self.to)


    class MessengerService:
        @staticmethod
        def has_replies(contact: NonPlayableCharacter):
            return contact.text_messages and hasattr(contact.text_messages[-1], "replies") and contact.text_messages[-1].replies

        @staticmethod
        def send_next_messages(contact: NonPlayableCharacter):
            while contact.pending_text_messages and not MessengerService.has_replies(contact):
                contact.pending_text_messages.pop(0).send()
