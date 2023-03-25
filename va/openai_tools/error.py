class InvalidMessageError(Exception):
    """
    Raised when a given message for chat-gpt request violates OpenAI's policy.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class TokenLimitError(Exception):
    """
    Raised when a query response runs out of tokens.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class NullResponseError(Exception):
    """
    Raised when a query response is null.
    """
    def __init__(self,
                 message: str = "For the given time, chat-gpt cannot process the given request. Please try again"):
        self.message = message
        super().__init__(self.message)