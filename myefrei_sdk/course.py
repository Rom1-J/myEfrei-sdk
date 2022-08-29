import logging
import typing

from .teacher import Teacher


if typing.TYPE_CHECKING:
    from .client import Client
    from .semester import Semester
    from .types.course import Course as CoursePayload


_log = logging.getLogger(__name__)


class Course:
    def __init__(self, client: "Client", data: "CoursePayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.teacher: list[Teacher] = self.__get_teachers(data["level1Name"])
        self.semester: "Semester" = self.__client.get_semester(
            data["custSemester"]
        )

        self.code: str = data["enrServiceId"]
        self.name: str = data["soffOfferingDesc"]

        self.scheduled: list["ScheduledCourse"] = []
        self.grades: list["Grade"] = []
        self.exam_papers: list["ExamPaper"] = []

    def __repr__(self) -> str:
        return (
            "<Course "
            "teacher=%s, "
            "semester=%s, "
            "code='%s', "
            "name='%s', "
            "scheduled=%s, "
            "grades=%s, "
            "exam_papers=%s>"
            % (
                str(self.teacher),
                str(self.semester),
                self.code,
                self.name,
                str(self.scheduled),
                str(self.grades),
                str(self.exam_papers),
            )
        )

    def __str__(self) -> str:
        return self.name

    # =========================================================================
    # =========================================================================

    def __get_teachers(self, data: str) -> list[Teacher]:
        if not data:
            return []

        return [
            Teacher(self.__client, teacher).add_course(self)
            for teacher in data.split(" - ")
        ]
