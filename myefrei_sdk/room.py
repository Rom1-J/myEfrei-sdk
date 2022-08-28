import datetime
import logging
import typing


if typing.TYPE_CHECKING:
    from .client import Client
    from .types.room import Room as RoomPayload


_log = logging.getLogger(__name__)


class Room:
    def __init__(self, client: "Client", data: "RoomPayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        h, m = data["st"].split("h")
        self.time: datetime.time = datetime.time(hour=int(h), minute=int(m))

        self.name: str = data["rn"]
        self.type: str = data["rt"]
        self.site: str = data["sn"]

    def __repr__(self) -> str:
        return (
            "<Room "
            "time=%s, "
            "name='%s', "
            "type='%s', "
            "site='%s'>"
            % (
                self.time,
                self.name,
                self.type,
                self.site,
            )
        )

    def __str__(self) -> str:
        return f"{self.name} ({self.type}) {self.time}"
