import typing


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


class User(typing.TypedDict):
    sub: str
    username: str
    firstname: str
    name: str
    fullname: str
    email: str
    email_verified: bool
    role: USER_ROLE
    home: str
    authorities: list[UserAuthority]


class Document(typing.TypedDict):
    docType: DOCUMENT_TYPE
    docFreeText: str
    docMimeType: str
    docSequenceNo: str
    docStatus: str
    docTitle: str
    docBlobFileGuid: str
    docBlobFileSize: str
    docPageGuid: str
    docPageLastUpdate: str
    docPageRevNo: str
    docTypeName: str
    stdNumber: str
