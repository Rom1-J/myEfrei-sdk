import logging
import typing


if typing.TYPE_CHECKING:
    from .client import Client
    from .student import Document

    from .types.semester import Semester as SemesterPayload


_log = logging.getLogger(__name__)


class Semester:
    def __init__(self, client: "Client", data: "SemesterPayload") -> None:
        self.__client: "Client" = client

        self.is_current: bool = bool(data.get("custCurrentSemester", False))

        self.name: str = data["custSemester"]
        self.year: int = int(data["custYearId"])
        self.year_gap: str = data["soffAcadPerId"]

        self.courses: list["Course"] = []
        self.scheduled_courses: list["ScheduledCourse"] = []

        self.grades: list["Grade"] = []
        self.documents: list["Document"] = []
        self.exam_papers: list["ExamPaper"] = []

    def __repr__(self) -> str:
        return (
            "<Semester "
            "is_current=%s, "
            "name='%s', "
            "year=%d>"
            % (
                str(self.is_current),
                self.name,
                self.year,
            )
        )

    def __str__(self) -> str:
        return f"{self.name} ({self.year_gap})"

    # =========================================================================

    async def complete(self) -> "Semester":
        return self
