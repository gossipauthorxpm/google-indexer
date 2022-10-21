class GoogleError(BaseException):
    def __init__(self, error: str):
        self.error: str = error

    def __str__(self):
        return self.error
