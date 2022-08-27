import logging
import typing

import aiohttp

from .student import Student


if typing.TYPE_CHECKING:
    from .types.student import Student as StudentPayload


_log = logging.getLogger(__name__)

BASE_URL = "https://www.myefrei.fr"


class Client:
    __student: Student | None = None

    # =========================================================================

    def __init__(self) -> None:
        self.__session: aiohttp.ClientSession | None = None

    async def connect(self, sid: str) -> None:
        self.__session = aiohttp.ClientSession(cookies={"myefrei.sid": sid})

        async with self.__session.get(BASE_URL + "/user") as response:
            self.student = await response.json()

    # =========================================================================
    # =========================================================================

    @property
    def student(self) -> Student | None:
        return self.__student

    @student.setter
    def student(self, data: "StudentPayload"):
        self.__student = Student(data)

    # =========================================================================
