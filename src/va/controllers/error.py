class InvalidKeyError(Exception):
    """
    Raised when a given list of keys are not valid for a chatty application.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)