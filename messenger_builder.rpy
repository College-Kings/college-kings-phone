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
            self.message_queue = MessageList()

        def __repr__(self):
            return f"PhoneMessage(from_={self.from_}, to={self.to})"

        def new_message(self, content: str):
            message = Message(content)
            if next_message is None:
                self.message_queue.append(message)
            else:
                self.message_queue.insertAfter(next_message, message)

            # Moves contact to the top when receiving a new message
            try:
                messenger.contacts.insert(
                    0, messenger.contacts.pop(messenger.contacts.index(self))
                )
            except ValueError:
                messenger.contacts.insert(0, self)

            self.notification = True

            return message

label start:
    python:
        builder = MessagerBuilder(mc, chloe)
        msg1 = builder.new_message("Hello, Chloe!")
        msg1.
