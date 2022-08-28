class ImproperApiResultException(ValueError):
    def __init__(self) -> None:
        message = "Improper data received from API"
        super().__init__(message)
