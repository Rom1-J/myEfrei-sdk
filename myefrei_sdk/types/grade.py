import typing


if typing.TYPE_CHECKING:
    from .course import Course, ScheduledCourse
    from .exam_paper import ExamPaper
    from .semester import Semester


GRADE_TYPE = typing.Literal["DE", "CE", "CO", "RAT", "TP", "CTD", "PRJ"]


class Grade(typing.TypedDict):
    is_approved: bool

    mark: float
    coef: float
    type: "GRADE_TYPE"

    course: "Course"
    exam: "ScheduledCourse"
    exam_paper: "ExamPaper"
    semester: "Semester"
