import typing


if typing.TYPE_CHECKING:
    from .course import Course, ScheduledCourse
    from .exam_paper import ExamPaper


class Teacher(typing.TypedDict):
    firstname: str
    lastname: str
    fullname: str

    courses: list["Course"]
    scheduled: list["ScheduledCourse"]
    exam_papers: list["ExamPaper"]
