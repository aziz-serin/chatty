class InvalidKeyError(Exception):
    """
    Raised when a given message for chat-gpt request contains an unsupoorted key.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)