import typing


class Notification(typing.TypedDict):
    number: int

    button: str
    description: str
    short_description: str
    title: str

    priority: str
    type: str
    url: str
