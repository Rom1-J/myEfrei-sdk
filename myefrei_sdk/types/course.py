import datetime
import typing


if typing.TYPE_CHECKING:
    from .exam_paper import ExamPaper
    from .grade import Grade
    from .semester import Semester
    from .teacher import Teacher


class ScheduledCourse(typing.TypedDict):
    pk: int

    teacher: list["Teacher"]

    room: str
    activity: str

    description: str
    category: str

    date: datetime.datetime
    start: datetime.datetime
    end: datetime.datetime


class Course(typing.TypedDict):
    id: str

    teacher: list["Teacher"]
    semester: "Semester"

    code: str
    name: str

    scheduled: list["ScheduledCourse"]
    grades: list["Grade"]
    exam_papers: list["ExamPaper"]
