import logging
import typing


if typing.TYPE_CHECKING:
    from .client import Client
    from .types.notification import Notification as NotificationPayload


_log = logging.getLogger(__name__)


class Notification:
    def __init__(self, client: "Client", data: "NotificationPayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.number: int = data["number"]

        self.button: str = data["btnDescription"]
        self.description: str = data["description"]
        self.short_description: str = data["shortDescription"]
        self.title: str = data["title"]

        self.priority: str = data["priority"]
        self.type: str = data["type"]
        self.url: str = data["url"]

    def __repr__(self) -> str:
        return (
            "<Notification "
            "title='%s', "
            "short_description='%s', "
            "priority='%s'>"
            % (
                self.title,
                self.short_description,
                self.priority,
            )
        )

    def __str__(self) -> str:
        return f"{self.title} ({self.priority})"
