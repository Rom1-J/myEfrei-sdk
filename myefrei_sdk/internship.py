import datetime
import logging
import typing


if typing.TYPE_CHECKING:
    from .client import Client
    from .types.internship import INTERNSHIP_STATE
    from .types.internship import Internship as InternshipPayload


_log = logging.getLogger(__name__)


class Internship:
    def __init__(self, client: "Client", data: "InternshipPayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.firm: str = data["custFirmContact"]

        self.start: datetime.datetime = datetime.datetime.fromisoformat(
            data["internshipDateFrom"]
        )
        self.end: datetime.datetime = datetime.datetime.fromisoformat(
            data["internshipDateTo"]
        )

        self.subject: str = data["internshipSubject"]
        self.state: "INTERNSHIP_STATE" = data["internshipProposalStage"]

    def __repr__(self) -> str:
        return (
            "<Internship "
            "firm='%s', "
            "start=%s, "
            "end=%s, "
            "subject='%s', "
            "state='%s'>"
            % (
                self.firm,
                str(self.start),
                str(self.end),
                self.subject,
                self.state,
            )
        )

    def __str__(self) -> str:
        return f"{self.firm} ({self.subject})"
