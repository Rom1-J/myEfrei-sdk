import datetime
import logging
import typing

import typing_extensions


if typing.TYPE_CHECKING:
    from .client import Client
    from .types.slide import SLIDE_TYPE
    from .types.slide import Slide as SlidePayload


_log = logging.getLogger(__name__)


class Slide:
    def __init__(self, client: "Client", data: "SlidePayload") -> None:
        self.__client: "Client" = client

        self.token: str = data["token"]

        self.author: str = data["author"]
        self.title: str = data["title"]
        self.text: str = data.get("text")
        self.type: "SLIDE_TYPE" = data.get("type")

        self.url: str | None = data.get("url")

        self.updated_at: datetime.datetime = datetime.datetime.fromisoformat(
            data["updateDate"]
        )

    def __repr__(self) -> str:
        return (
            "<Slide "
            "token=%s, "
            "author=%s, "
            "title=%s>"
            % (
                self.token,
                self.author,
                self.title,
            )
        )

    def __str__(self) -> str:
        return f"{self.title} ({self.author})"

    # =========================================================================

    async def complete(self) -> typing_extensions.Self:
        return await self.__client.fetch_slide(self.token)
