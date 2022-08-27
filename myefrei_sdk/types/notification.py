import typing


class Notification(typing.TypedDict):
    button_description: str
    description: str
    short_description: str
    title: str

    number: int
    priority: str
    type: str
    url: str
