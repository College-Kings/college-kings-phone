init python:
    class MessengerBuilder:
        def __init__(self, character: NonPlayableCharacter, target: PlayableCharacter):
            self.character = character
            self.target = target
            self.history = []

        def new_message(self, content: str = ""):
            message = Message(self, content)

            # Moves contact to the top when receiving a new message
            try:
                messenger.contacts.insert(
                    0, messenger.contacts.pop(messenger.contacts.index(self))
                )
            except ValueError:
                messenger.contacts.insert(0, self)

            # Add message to queue
            self.sent_messages.append(message)
            self.pending_messages = []

            # self.notification = True

            return self

        def new_image_message(self, image: str):
            message = ImageMessage(self, image)

            # Moves contact to the top when receiving a new message
            try:
                messenger.contacts.insert(
                    0, messenger.contacts.pop(messenger.contacts.index(self))
                )
            except ValueError:
                messenger.contacts.insert(0, self)

            # Add message to queue
            self.sent_messages.append(message)
            self.pending_messages = []

            # self.notification = True

            return self

        def add_reply(
            self,
            content: str,
            func: Optional[Callable[[], None]] = None,
        ):
            reply = Reply(content, func)

            # Append reply to last sent message
            try:
                if in_reply:
                    self.sent_messages[-1].replies.append(reply)
                elif self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                elif self.sent_messages:
                    self.sent_messages[-1].replies.append(reply)
                else:
                    message = self.new_message("", force_send=True)
                    message.replies.append(reply)
            except IndexError:
                message = self.new_message("", force_send=True)
                message.replies.append(reply)

            self.notification = True

        def add_image_reply(
            self,
            content: str,
            func: Optional[Callable[[], None]] = None,
            new_message: bool = False,
        ):
            reply = ImgReply(content, func)

            # Append reply to last sent message
            try:
                if new_message:
                    message = self.new_message("")
                    message.replies.append(reply)
                elif self.pending_messages:
                    self.pending_messages[-1].replies.append(reply)
                else:
                    self.sent_messages[-1].replies.append(reply)
            except IndexError:
                message = self.new_message("", force_send=True)
                message.replies.append(reply)

            self.notification = True