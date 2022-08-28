import datetime
import logging
import typing


if typing.TYPE_CHECKING:
    from .client import Client
    from .types.absence import Absence as AbsencePayload

_log = logging.getLogger(__name__)


class Absence:
    def __init__(self, client: "Client", data: "AbsencePayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.excused: str = data["stdAbsExcused"]

        self.course: typing.Optional["ScheduledCourse"]
        self.course_name: str = data["actCodDescription"]
        self.course_description: str = data["soffOfferingDesc"]

        self.date: datetime.datetime = datetime.datetime.fromisoformat(
            data["stdAbsClassDate"]
        )
        self.hours: float = float(data["timeCrAbsHours"])
        self.start: datetime.datetime
        self.end: datetime.datetime

        self.semester: "Semester"

    def __repr__(self) -> str:
        return (
            "<Absence "
            "excused=%s, "
            "course=%s, "
            "date=%s, "
            "hours=%s, "
            "start=%s, "
            "end=%s,"
            "semester=%s>"
            % (
                self.excused,
                str(self.course),
                str(self.date),
                str(self.hours),
                str(self.start),
                str(self.end),
                str(self.semester),
            )
        )

    def __str__(self) -> str:
        return "%s (%d)" % (str(self.course), str(self.excused))

    # =========================================================================
    # =========================================================================

    @property
    def is_excused(self) -> bool:
        return self.excused == "Excusée"
