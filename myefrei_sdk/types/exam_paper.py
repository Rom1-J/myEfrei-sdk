import datetime
import typing


if typing.TYPE_CHECKING:
    from .course import Course, ScheduledCourse
    from .teacher import Teacher


EXAM_TYPE = typing.Literal["DE", "CE", "RAT"]


class ExamPaper(typing.TypedDict):
    create_date: datetime.datetime
    exam_date: datetime.datetime

    file_name: str
    exam_type: "EXAM_TYPE"

    course: "Course"
    exam: "ScheduledCourse"
    teachers: list["Teacher"]
