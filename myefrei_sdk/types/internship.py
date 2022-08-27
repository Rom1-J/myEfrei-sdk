import datetime
import typing


if typing.TYPE_CHECKING:
    from .semester import Semester


INTERNSHIP_STATE = typing.Literal["INITIE", "ACCEPTE"]


class Internship(typing.TypedDict):
    pk: str
    id: str

    firm: str

    start: datetime.datetime
    end: datetime.datetime
    semester: "Semester"

    subject: str
    state: "INTERNSHIP_STATE"
