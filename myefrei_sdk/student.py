import typing


if typing.TYPE_CHECKING:
    from .types.student import USER_ROLE
    from .types.student import Student as StudentPayload
    from .types.student import UserAuthority


class Student:
    def __init__(self, data: "StudentPayload") -> None:
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
            "<Student "
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
