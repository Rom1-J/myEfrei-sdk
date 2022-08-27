import datetime
import typing
import uuid


AUTHORITY_TYPE = typing.Literal[
    "ROLE_USER",
    "ROLE_STUDENT",
    "EXTRANET",
    "PORTAL",
    "API",
    "STUDAPART",
    "STUDEAL",
    "APPSCHO",
    "JOBTEASER",
]
DOCUMENT_TYPE = typing.Literal["DOCADMIN", "RESULTS.ACAD"]
USER_ROLE = typing.Literal["admin", "student", "teacher", "candidate", "guest"]


class UserAuthority(typing.TypedDict):
    authority: AUTHORITY_TYPE


class Student(typing.TypedDict):
    sub: int
    username: str

    firstname: str
    lastname: str
    fullname: str

    authorities: list[UserAuthority]

    email: str
    email_verified: bool

    home: str
    role: USER_ROLE


class Document(typing.TypedDict):
    id: int
    file_guid: uuid.UUID
    page_guid: uuid.UUID

    type: DOCUMENT_TYPE
    type_name: str
    mimetype: str
    status: str
    title: str
    size: int

    page_last_updated: datetime.datetime
    page_revision_number: int
