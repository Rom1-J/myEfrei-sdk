import logging

import aiohttp

from ._constants import API_URL, BASE_URL
from .absence import Absence
from .error import ImproperApiResultException
from .notification import Notification
from .pave import Pave
from .semester import Semester
from .slide import Slide
from .student import Document, User


_log = logging.getLogger(__name__)


class Client:
    __user: User | None = None
    __pave: Pave

    __documents: list[Document] | None = None
    __absences: list[Absence] | None = None
    __notifications: list[Notification] | None = None
    __slides: list[Slide] | None = None
    __semesters: list[Semester] | None = None

    # =========================================================================

    def __init__(self) -> None:
        self.__session: aiohttp.ClientSession = aiohttp.ClientSession()

    async def connect(self, sid: str, fetch_all: bool = False) -> None:
        self.__session = aiohttp.ClientSession(cookies={"myefrei.sid": sid})
        self.__pave = Pave(self, self.__session)

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
                    await Semester(self, raw_data).complete()
                    for raw_data in data.get("rows", [])
                ]
                return self.semesters or []

            raise ImproperApiResultException()
