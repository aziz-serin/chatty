class AppConstructionError(Exception):
    """
    Raised when construction of the flask app is failed
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConnectionConstructionError(Exception):
    """
    Raised when construction of the flask app is failed
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
