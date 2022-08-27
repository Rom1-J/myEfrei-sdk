import datetime
import typing


class Slide(typing.TypedDict):
    author: str
    title: str
    token: str
    update_date: datetime.datetime
