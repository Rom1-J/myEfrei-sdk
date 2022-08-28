import logging

import aiohttp

from .absence import Absence
from .error import ImproperApiResultException
from .slide import Slide
from .student import Document, User


_log = logging.getLogger(__name__)

BASE_URL = "https://www.myefrei.fr"
API_URL = BASE_URL + "/api"


class Client:
    __user: User | None = None
    __documents: list[Document] | None = None
    __absences: list[Absence] | None = None
    __slides: list[Slide] | None = None

    # =========================================================================

    def __init__(self) -> None:
        self.__session: aiohttp.ClientSession | None = None

    async def connect(self, sid: str) -> None:
        self.__session = aiohttp.ClientSession(cookies={"myefrei.sid": sid})

        async with self.__session.get(BASE_URL + "/user") as response:
            self.__user = User(self, await response.json())

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
                return self.documents

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
                return self.absences

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
                return self.slides

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
            Asked myEfrei slides
        """
        endpoint = f"{API_URL}/rest/common/slides/{token}"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                return Slide(self, data)

            raise ImproperApiResultException()
