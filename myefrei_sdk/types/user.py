import typing


AuthorityType = typing.Literal[
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


class UserAuthority(typing.TypedDict):
    authority: AuthorityType


class User(typing.TypedDict):
    authorities: list[UserAuthority]

    email: str
    email_verified: bool

    firstname: str
    name: str
    fullname: str
    username: str
    sub: int

    home: str
    role: str
