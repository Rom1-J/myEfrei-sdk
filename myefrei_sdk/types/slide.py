import datetime
import typing


SLIDE_TYPE = typing.Literal["html", "url"]


class Slide(typing.TypedDict):
    token: str

    author: str
    title: str
    text: str
    type: SLIDE_TYPE

    url: str | None

    updated_at: datetime.datetime
