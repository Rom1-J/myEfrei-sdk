import typing


class Notification(typing.TypedDict):
    type: str
    number: int
    title: str
    description: str
    shortDescription: str
    btnDescription: str
    url: str
    priority: str
