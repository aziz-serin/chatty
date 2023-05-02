class InvalidMessageError(BaseException):
    """
    Raised when a given message for chat-gpt request violates OpenAI's policy.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class TokenLimitError(BaseException):
    """
    Raised when a query response runs out of tokens.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class NullResponseError(BaseException):
    """
    Raised when a query response is null.
    """
    def __init__(self,
                 message: str = "For the given time, chat-gpt cannot process the given request. Please try again"):
        self.message = message
        super().__init__(self.message)

class FileSizeError(BaseException):
    """
    Raised when given audio file size is larger than the limit placed by OpenAI (25Mb)
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class VAError(BaseException):
    """
    Raised when the code execution encounters other errors, e.g. OpenAIError, OSError
    """
    def __init__(self, cause):
        self.message = cause
        super().__init__(self.message)

class OpenAIAPIKeyError(BaseException):
    """
    Raised when env variable for openai api key is not set.
    """
    def __init__(self, cause):
        self.message = cause
        super().__init__(self.message)
