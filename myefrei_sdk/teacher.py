import logging
import typing


if typing.TYPE_CHECKING:
    from .client import Client
    from .course import Course

_log = logging.getLogger(__name__)


class Teacher:
    def __init__(self, client: "Client", data: str) -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        lastname, firstname = data.split(", ")

        self.firstname: str = firstname
        self.lastname: str = lastname.upper()
        self.fullname: str = f"{self.firstname} {self.lastname}"

        self.courses: list["Course"] = []
        self.scheduled: list["ScheduledCourse"] = []
        self.exam_papers: list["ExamPaper"] = []

    def __repr__(self) -> str:
        return (
            "<Teacher "
            "firstname=%s, "
            "lastname=%s, "
            "fullname='%s', "
            "courses=%s, "
            "scheduled=%s, "
            "exam_papers=%s>"
            % (
                self.firstname,
                self.lastname,
                self.fullname,
                str(self.courses),
                str(self.scheduled),
                str(self.exam_papers),
            )
        )

    def __str__(self) -> str:
        return self.fullname

    # =========================================================================

    def add_course(self, course: "Course") -> "Teacher":
        if course not in self.courses:
            self.courses.append(course)

        return self
