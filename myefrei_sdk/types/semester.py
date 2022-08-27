import typing


if typing.TYPE_CHECKING:
    from .course import Course, ScheduledCourse
    from .exam_paper import ExamPaper
    from .grade import Grade
    from .student import Document


class Semester(typing.TypedDict):
    is_current: bool

    name: str
    year: int
    year_gap: str

    courses: list["Course"]
    scheduled_courses: list["ScheduledCourse"]

    grades: list["Grade"]
    documents: list["Document"]
    exam_papers: list["ExamPaper"]
