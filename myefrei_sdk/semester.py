import logging
import typing

import aiohttp

from ._constants import API_URL
from .absence import Absence
from .error import ImproperApiResultException


if typing.TYPE_CHECKING:
    from .client import Client
    from .student import Document
    from .types.semester import Semester as SemesterPayload


_log = logging.getLogger(__name__)


class Semester:
    __absences: list[Absence] | None = None

    # =========================================================================

    def __init__(
        self,
        client: "Client",
        session: aiohttp.ClientSession,
        data: "SemesterPayload",
    ) -> None:
        self.__client: "Client" = client
        self.__session: aiohttp.ClientSession = session

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
    # =========================================================================

    async def complete(self) -> "Semester":
        return self

    # =========================================================================

    @property
    def absences(self) -> list[Absence] | None:
        return self.__absences

    # =========================================================================

    async def fetch_absences(self) -> list[Absence]:
        """Retrieves an :term:`iterator` containing semester absences.

        Examples
        ---------
        Usage ::
            for absences in await client.get_semester("S6").fetch_absences():
                print(len(absences))

        Raises
        ------
        HTTPException
            Getting the semester absences failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Absences`]
            All semester absences.
        """
        endpoint = (
            f"{API_URL}"
            "/extranet/student/queries/student-absences"
            f"?yearId={self.year}"
        )

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__absences = [
                    Absence(self.__client, raw_data)
                    for raw_data in data.get("rows", [])
                ]
                return self.absences or []

            raise ImproperApiResultException()
