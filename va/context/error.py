class ContextConstructionError(Exception):
    """
    Raised when construction of the app context is failed
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConnectionConstructionError(Exception):
    """
    Raised when construction of the connection is failed
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
