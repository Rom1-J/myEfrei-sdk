import asyncio
import datetime
import logging
import typing

import aiohttp

from ._constants import API_URL, BASE_URL
from .absence import Absence
from .course import Course
from .error import ImproperApiResultException
from .internship import Internship
from .notification import Notification
from .pave import Pave
from .room import Room
from .semester import Semester
from .slide import Slide
from .student import Document, User


if typing.TYPE_CHECKING:
    from types import TracebackType

_log = logging.getLogger(__name__)


# pylint: disable=too-many-public-methods
class Client:
    __user: User | None = None
    __pave: Pave

    __documents: list[Document] | None = None
    __absences: list[Absence] | None = None
    __notifications: list[Notification] | None = None
    __slides: list[Slide] | None = None
    __semesters: list[Semester] | None = None
    __internships: list[Internship] | None = None
    __courses: list[Course] | None = None

    # =========================================================================

    def __init__(
        self, sid: str, loop: asyncio.AbstractEventLoop | None = None
    ) -> None:
        self.__loop: asyncio.AbstractEventLoop = (
            loop or asyncio.get_event_loop()
        )
        self.__session = aiohttp.ClientSession(
            cookies={"myefrei.sid": sid}, loop=self.__loop
        )

        self.__pave = Pave(self, self.__session)

    # =========================================================================

    async def __aenter__(self) -> "Client":
        await self.connect()

        return self

    # =========================================================================

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: typing.Optional["TracebackType"],
    ) -> None:
        if not self.__session.closed:
            await self.disconnect()

    # =========================================================================
    # =========================================================================

    async def connect(self, fetch_all: bool = False) -> None:
        async with self.__session.get(BASE_URL + "/user") as response:
            self.__user = User(self, await response.json())

        if fetch_all:
            await self.fetch_semesters()
            await self.fetch_slides()
            await self.fetch_notifications()
            await self.fetch_documents()

            await self.pave.fetch_interests()
            await self.pave.fetch_roles()
            await self.pave.fetch_associations()
            await self.pave.fetch_mines()

    # =========================================================================

    async def disconnect(self) -> None:
        await self.__session.close()

    # =========================================================================
    # =========================================================================

    @property
    def user(self) -> User | None:
        return self.__user

    # =========================================================================

    @property
    def documents(self) -> list[Document] | None:
        return self.__documents

    # =========================================================================

    @property
    def absences(self) -> list[Absence] | None:
        return self.__absences

    # =========================================================================

    @property
    def slides(self) -> list[Slide] | None:
        return self.__slides

    # =========================================================================

    @property
    def notifications(self) -> list[Notification] | None:
        return self.__notifications

    # =========================================================================

    @property
    def pave(self) -> Pave:
        return self.__pave

    # =========================================================================

    @property
    def semesters(self) -> list[Semester] | None:
        return self.__semesters

    def get_semester(self, name: str) -> Semester | None:
        if self.semesters:
            return next(
                filter(
                    lambda s: s.name.lower() == name.lower(), self.semesters
                ),
                None,
            )

        return None

    # =========================================================================

    @property
    def courses(self) -> list[Course] | None:
        return self.__courses

    def get_course(self, q: str) -> Course | None:
        if self.courses:
            return next(
                filter(lambda c: q in (c.code, c.name), self.courses),
                None,
            )

        return None

    # =========================================================================

    @property
    def internships(self) -> list[Internship] | None:
        return self.__internships

    # =========================================================================
    # =========================================================================

    async def fetch_documents(self) -> list[Document]:
        """Retrieves an :term:`iterator` containing student documents.

        Examples
        ---------
        Usage ::
            for document in await client.fetch_documents():
                print(document.type)

        Raises
        ------
        HTTPException
            Getting the documents failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Document`]
            All available documents.
        """
        endpoint = f"{API_URL}/extranet/student/queries/student-documents"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__documents = [
                    Document(self, raw_data)
                    for raw_data in data.get("rows", [])
                ]
                return self.documents or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_absences(self, year: int) -> list[Absence]:
        """Retrieves an :term:`iterator` containing student absences.

        Examples
        ---------
        Usage ::
            for absence in await client.fetch_absences():
                print(document.type)

        Parameters
        -----------
        year: :class:`int`
            The year to fetch from.

        Raises
        ------
        HTTPException
            Getting the absences failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Document`]
            All student absences.
        """
        endpoint = (
            f"{API_URL}"
            f"/extranet/student/queries/student-absences?yearId={year}"
        )

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__absences = [
                    Absence(self, raw_data)
                    for raw_data in data.get("rows", [])
                ]
                return self.absences or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_notifications(self) -> list[Notification]:
        """Retrieves an :term:`iterator` containing myEfrei notifications.

        Examples
        ---------
        Usage ::
            for notification in await client.fetch_notifications():
                print(notification.title)

        Raises
        ------
        HTTPException
            Getting the notifications failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Notification`]
            All myEfrei notifications.
        """
        endpoint = f"{API_URL}/rest/student/notifications"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), list):
                self.__notifications = [
                    Notification(self, raw_data) for raw_data in data
                ]
                return self.notifications or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_slides(self) -> list[Slide]:
        """Retrieves an :term:`iterator` containing myEfrei slides.

        Examples
        ---------
        Usage ::
            for slide in await client.fetch_slides():
                print(slide.title)

        Raises
        ------
        HTTPException
            Getting the slides failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Slide`]
            All myEfrei slides.
        """
        endpoint = f"{API_URL}/rest/common/slides"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), list):
                self.__slides = [
                    await Slide(self, raw_data).complete() for raw_data in data
                ]
                return self.slides or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_slide(self, token: str) -> Slide:
        """Retrieves a specific myEfrei slides.

        Examples
        ---------
        Usage ::
            slide = await client.fetch_slide("owpbmdrzopembyhm")
            print(slide.title)

        Parameters
        -----------
        token: :class:`str`
            Slide token to fetch from.

        Raises
        ------
        HTTPException
            Getting the slide failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        :class:`.Slide`
            Asked myEfrei slides.
        """
        endpoint = f"{API_URL}/rest/common/slides/{token}"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                return Slide(self, data)  # type: ignore[arg-type]

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_semesters(self) -> list[Semester]:
        """Retrieves an :term:`iterator` containing myEfrei notifications.

        Examples
        ---------
        Usage ::
            for notification in await client.fetch_notifications():
                print(notification.title)

        Raises
        ------
        HTTPException
            Getting the notifications failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Notification`]
            All myEfrei notifications.
        """
        endpoint = f"{API_URL}/extranet/student/queries/student-semesters"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__semesters = [
                    await Semester(self, self.__session, raw_data).complete()
                    for raw_data in data.get("rows", [])
                ]
                return self.semesters or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_rooms(self, date: datetime.datetime) -> list[Room]:
        """Retrieves an :term:`iterator` containing available rooms.

        Examples
        ---------
        Usage ::
            date = datetime.datetime.now()
            for room in await client.fetch_rooms(date):
                print(room.name)

        Raises
        ------
        HTTPException
            Getting the rooms failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Room`]
            All available rooms.
        """
        endpoint = (
            f"{API_URL}"
            "/extranet/queries/free-rooms"
            f"?date={date.strftime('%Y-%m-%d')}"
        )

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                rooms = [
                    Room(self, raw_data) for raw_data in data.get("rows", [])
                ]
                return rooms or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_internships(self) -> list[Internship]:
        """Retrieves an :term:`iterator` containing all internships.

        Examples
        ---------
        Usage ::
            for internship in await client.fetch_internships(date):
                print(internship.subject)

        Raises
        ------
        HTTPException
            Getting the internships failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Internship`]
            All internships.
        """
        endpoint = f"{API_URL}/extranet/student/queries/internships"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__internships = [
                    Internship(self, raw_data)
                    for raw_data in data.get("rows", [])
                ]
                return self.internships or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_courses(self, semester: Semester) -> list[Course]:
        """Retrieves an :term:`iterator` containing all courses.

        Examples
        ---------
        Usage ::
            semester = client.get_semester("S6")
            for course in await client.fetch_courses(semester):
                print(course.name)

        Raises
        ------
        HTTPException
            Getting the courses failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.Internship`]
            All courses for given semester.
        """
        endpoint = (
            f"{API_URL}"
            f"/extranet/student/queries/student-moodle-courses"
            f"?semester={semester.name}"
            f"&year={semester.year_gap}"
        )

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__courses = [
                    Course(self, raw_data)
                    for raw_data in filter(
                        lambda c: c["soffServiceGrpId"] == "MODULE",
                        data.get("rows", []),
                    )
                ]
                return self.courses or []

            raise ImproperApiResultException()
