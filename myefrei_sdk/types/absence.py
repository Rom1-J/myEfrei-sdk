import datetime
import typing


if typing.TYPE_CHECKING:
    from .course import ScheduledCourse
    from .semester import Semester


class Absence(typing.TypedDict):
    is_excused: bool

    course: typing.Optional["ScheduledCourse"]
    course_name: str
    course_description: str

    date: datetime.datetime
    hours: float
    start: datetime.datetime
    end: datetime.datetime

    semester: "Semester"
