init python:
    class BaseMessage:
        def __init__(self, contact: Contact, content: str):
            self.contact = contact
            self.content = content
            self.message = content
            self.image = content
            self.replies: list[BaseReply] = []
            self.reply: Optional[BaseReply] = None

        def __repr__(self):
            return f"<{self.__class__.__name__}({self.content})>"


    class Reply(BaseMessage):
        def __init__(
            self,
            message: str,
            func: Optional[Callable[[], None]] = None,
        ):
            super().__init__(mc, message)

            self.func = func


    class ImgReply(BaseMessage):
        def __init__(
            self,
            image: str,
            func: Optional[Callable[[], None]] = None,
        ):
            super().__init__(mc, image)

            self.func = func


    class Message(BaseMessage):
        def __init__(self, contact: Contact, message: str):
            super().__init__(contact, message)


    class ImageMessage(BaseMessage):
        def __init__(self, contact: Contact, image: str):
            super().__init__(contact, image)


    BaseReply = Union[Reply, ImgReply]
