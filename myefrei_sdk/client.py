import logging

import aiohttp

from .student import Document, User


_log = logging.getLogger(__name__)

BASE_URL = "https://www.myefrei.fr"
API_URL = BASE_URL + "/api"


class Client:
    __user: User | None = None

    # =========================================================================

    def __init__(self) -> None:
        self.__session: aiohttp.ClientSession | None = None

    async def connect(self, sid: str) -> None:
        self.__session = aiohttp.ClientSession(cookies={"myefrei.sid": sid})

        async with self.__session.get(BASE_URL + "/user") as response:
            self.__user = User(await response.json())

    # =========================================================================
    # =========================================================================

    @property
    def user(self) -> User | None:
        return self.__user

    # =========================================================================

    async def fetch_documents(self) -> list[Document]:
        """Retrieves an :term:`asynchronous iterator` containing student
        documents.

        Examples
        ---------
        Usage ::
            for document in await client.fetch_documents():
                print(document.type)

        Raises
        ------
        HTTPException
            Getting the documents failed.

        ValueError
            Data retrieved from API are improper to parsing.

        Yields
        --------
        :class:`.Document`
            The parsed document.
        """

        async with self.__session.get(
            API_URL + "/extranet/student/queries/student-documents"
        ) as response:
            if isinstance((data := await response.json()), dict):
                return [
                    Document(raw_data)
                    for raw_data in data.get("rows", [])
                ]

            raise ValueError("Improper data received from API")
