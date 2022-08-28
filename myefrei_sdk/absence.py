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

        self.course: typing.Optional["ScheduledCourse"] = None
        self.course_name: str = data["actCodDescription"]
        self.course_description: str = data["soffOfferingDesc"]

        self.date: datetime.datetime = datetime.datetime.fromisoformat(
            data["stdAbsClassDate"]
        )
        self.hours: float = float(data["timeCrAbsHours"])
        self.start: datetime.datetime = self._get_block(data["timeCrBlockId"])[
            0
        ]
        self.end: datetime.datetime = self._get_block(data["timeCrBlockId"])[1]

    def __repr__(self) -> str:
        return (
            "<Absence "
            "excused='%s', "
            "course=%s, "
            "date='%s', "
            "hours='%s', "
            "start='%s', "
            "end='%s'>"
            % (
                self.excused,
                repr(self.course),
                str(self.date),
                str(self.hours),
                str(self.start),
                str(self.end),
            )
        )

    def __str__(self) -> str:
        return f"{str(self.course)} ({self.excused})"

    # =========================================================================

    def _get_block(
        self, block: str
    ) -> tuple[datetime.datetime, datetime.datetime]:
        def to_time(hour: str) -> datetime.time:
            h, m = hour.split("H")

            return datetime.time(hour=int(h), minute=int(m))

        start = to_time(block.split("-")[0])
        end = to_time(block.split("-")[1])

        return (
            self.date
            + datetime.timedelta(hours=start.hour, minutes=start.minute),
            self.date + datetime.timedelta(hours=end.hour, minutes=end.minute),
        )

    # =========================================================================
    # =========================================================================

    @property
    def is_excused(self) -> bool:
        return self.excused == "Excusée"
