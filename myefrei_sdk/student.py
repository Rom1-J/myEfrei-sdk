import datetime
import logging
import typing
import uuid


if typing.TYPE_CHECKING:
    from .client import Client
    from .types.student import DOCUMENT_TYPE, USER_ROLE
    from .types.student import Document as DocumentPayload
    from .types.student import User as StudentPayload
    from .types.student import UserAuthority


_log = logging.getLogger(__name__)


class User:
    def __init__(self, client: "Client", data: "StudentPayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.sub: int = int(data["sub"])
        self.username: str = data["username"]

        self.firstname: str = data["firstname"]
        self.lastname: str = data["name"]
        self.fullname: str = data["fullname"]

        self.email: str = data["email"]
        self.is_email_verified: bool = bool(data["email_verified"])

        self.role: "USER_ROLE" = data["role"]
        self.home: str = data["home"]

        self.authorities: list["UserAuthority"] = data["authorities"]

    def __repr__(self) -> str:
        return (
            "<User "
            "sub=%d, "
            "firstname=%s, "
            "lastname=%s, "
            "email=%s, "
            "is_email_verified=%s, "
            "role=%s,"
            "authorities=%s>"
            % (
                self.sub,
                self.firstname,
                self.lastname,
                self.email,
                str(self.is_email_verified),
                self.role,
                str(self.authorities),
            )
        )

    def __str__(self) -> str:
        return "%s (%d)" % (self.fullname, self.sub)


class Document:
    def __init__(self, client: "Client", data: "DocumentPayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.id: int = int(data["docSequenceNo"])
        self.file_guid: uuid.UUID = uuid.UUID(data["docBlobFileGuid"])
        self.page_guid: uuid.UUID = uuid.UUID(data["docPageGuid"])

        self.type: "DOCUMENT_TYPE" = data["docType"]
        self.type_name: str = data["docTypeName"]
        self.mimetype: str = data["docMimeType"]
        self.status: str = data["docStatus"]
        self.title: str = data["docTitle"]
        self.size: int = int(data["docBlobFileSize"])

        self.page_last_updated: datetime.datetime = (
            datetime.datetime.fromisoformat(data["docPageLastUpdate"])
        )
        self.page_revision_number: int = int(data["docPageRevNo"])

    def __repr__(self) -> str:
        return (
            "<Document "
            "id=%d, "
            "title=%s, "
            "type_name=%s, "
            "mimetype=%s, "
            "size=%d, "
            "page_last_updated=%s>"
            % (
                self.id,
                self.title,
                self.type_name,
                self.mimetype,
                self.size,
                str(self.page_last_updated),
            )
        )

    def __str__(self) -> str:
        return "%s (%d)" % (self.title, self.size)
