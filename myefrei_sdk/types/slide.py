import typing


SLIDE_TYPE = typing.Literal["html", "url"]


class Slide(typing.TypedDict):
    title: str
    type: SLIDE_TYPE
    author: str
    text: str
    url: str
    updateDate: str
    token: str
