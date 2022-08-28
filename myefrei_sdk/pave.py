import logging
import typing

import aiohttp

from ._constants import API_URL
from .error import ImproperApiResultException
from .semester import Semester


if typing.TYPE_CHECKING:
    from .client import Client
    from .types.pave import ROLE, TIME
    from .types.pave import Association as AssociationPayload
    from .types.pave import Interest as InterestPayload
    from .types.pave import Pave as StudentPavePayload
    from .types.pave import Role as RolePayload

_log = logging.getLogger(__name__)


class PaveAssociation:
    def __init__(self, client: "Client", data: "AssociationPayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.id: int = int(data["id"])
        self.name = data["name"]

    def __repr__(self) -> str:
        return "<PaveAssociation id=%d, name='%s'>" % (self.id, self.name)

    def __str__(self) -> str:
        return self.name


class PaveRole:
    def __init__(self, client: "Client", data: "RolePayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.id: int = int(data["id"])
        self.name: "ROLE" = data["name"]

    def __repr__(self) -> str:
        return "<PaveRole id=%d, name='%s'>" % (self.id, self.name)

    def __str__(self) -> str:
        return self.name


class PaveInterest:
    def __init__(self, client: "Client", data: "InterestPayload") -> None:
        # pylint: disable=unused-private-member
        self.__client: "Client" = client

        self.id: int = int(data["id"])
        self.time: "TIME" = data["time"]

    def __repr__(self) -> str:
        return "<PaveInterest id=%d, time='%s'>" % (self.id, self.time)

    def __str__(self) -> str:
        return self.time


class PaveStudent:
    def __init__(self, client: "Client", data: "StudentPavePayload") -> None:
        self.__client: "Client" = client

        self.id: int = data["id"]
        self.association: PaveAssociation | None = (
            self.__client.pave.get_association(data["associationId"])
        )

        self.role: PaveRole | None = self.__client.pave.get_role(
            data["roleId"]
        )
        self.other_role: str | None = data.get("otherRole")

        self.invested: PaveInterest | None = self.__client.pave.get_interest(
            data["investedTime"]
        )

        self.mission: str = data["mission"]
        self.acquired_skills: str = data["acquiredSkills"]
        self.motivation: str = data["motivation"]

        self.mark: int = data["mark"]
        self.public_comment: str | None = data.get("publicComment")

    def __repr__(self) -> str:
        return (
            "<PaveStudent id=%d, "
            "association=%s, "
            "role=%s, "
            "invested=%s,"
            "mark=%d >"
            % (
                self.id,
                repr(self.association),
                repr(self.role),
                repr(self.invested),
                self.mark,
            )
        )

    def __str__(self) -> str:
        return f"{self.role} ({self.association}) {self.mark}"


class Pave:
    __associations: list[PaveAssociation] | None = None
    __roles: list[PaveRole] | None = None
    __interests: list[PaveInterest] | None = None
    __mines: list[PaveStudent] | None = None

    # =========================================================================

    def __init__(
        self, client: "Client", session: aiohttp.ClientSession
    ) -> None:
        self.__client: "Client" = client
        self.__session: aiohttp.ClientSession = session

    # =========================================================================
    # =========================================================================

    @property
    def associations(self) -> list[PaveAssociation] | None:
        return self.__associations

    def get_association(self, q: int | str) -> PaveAssociation | None:
        if self.associations:
            return next(
                filter(lambda a: q in (a.id, a.name), self.associations), None
            )

        return None

    # =========================================================================

    @property
    def roles(self) -> list[PaveRole] | None:
        return self.__roles

    def get_role(self, q: typing.Union[int, "ROLE"]) -> PaveRole | None:
        if self.roles:
            return next(
                filter(lambda r: q in (r.id, r.name), self.roles), None
            )

        return None

    # =========================================================================

    @property
    def interests(self) -> list[PaveInterest] | None:
        return self.__interests

    def get_interest(
        self, q: typing.Union[int, "TIME"]
    ) -> PaveInterest | None:
        if self.interests:
            return next(
                filter(lambda i: q in (i.id, i.time), self.interests), None
            )

        return None

    # =========================================================================

    @property
    def mines(self) -> list[PaveStudent] | None:
        return self.__mines

    # =========================================================================
    # =========================================================================

    async def fetch_associations(self) -> list[PaveAssociation]:
        """Retrieves an :term:`iterator` containing PAVE associations.

        Examples
        ---------
        Usage ::
            for association in await client.pave.fetch_associations():
                print(association.name)

        Raises
        ------
        HTTPException
            Getting the associations failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.PaveAssociation`]
            All PAVE associations.
        """
        endpoint = (
            f"{API_URL}" "/extranet/student/queries/paves/pave-associations"
        )

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__associations = [
                    PaveAssociation(self.__client, raw_data)
                    for raw_data in data.get("rows", [])
                ]
                return self.associations or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_roles(self) -> list[PaveRole]:
        """Retrieves an :term:`iterator` containing PAVE roles.

        Examples
        ---------
        Usage ::
            for role in await client.pave.fetch_roles():
                print(role.name)

        Raises
        ------
        HTTPException
            Getting the roles failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.PaveRole`]
            All PAVE roles.
        """
        endpoint = f"{API_URL}" "/extranet/student/queries/paves/pave-roles"

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__roles = [
                    PaveRole(self.__client, raw_data)
                    for raw_data in data.get("rows", [])
                ]
                return self.roles or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_interests(self) -> list[PaveInterest]:
        """Retrieves an :term:`iterator` containing PAVE interests.

        Examples
        ---------
        Usage ::
            for interest in await client.pave.fetch_interests():
                print(interest.time)

        Raises
        ------
        HTTPException
            Getting the interests failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.PaveInterest`]
            All PAVE interests.
        """
        endpoint = (
            f"{API_URL}" "/extranet/student/queries/paves/pave-invested-times"
        )

        async with self.__session.get(endpoint) as response:
            if isinstance((data := await response.json()), dict):
                self.__interests = [
                    PaveInterest(self.__client, raw_data)
                    for raw_data in data.get("rows", [])
                ]
                return self.interests or []

            raise ImproperApiResultException()

    # =========================================================================

    async def fetch_mines(
        self, semester: Semester | None = None
    ) -> list[PaveStudent]:
        """Retrieves an :term:`iterator` containing PAVE done in given
        semester.

        Examples
        ---------
        Usage ::
            for interest in await client.pave.fetch_interests():
                print(interest.time)

        Raises
        ------
        HTTPException
            Getting the interests failed.

        ImproperApiResultException
            Data retrieved from API are improper to parsing.

        Return
        -------
        List[:class:`.PaveInterest`]
            All PAVE interests.
        """
        if semester:
            endpoint = (
                f"{API_URL}"
                "/extranet/student/queries/paves/student-paves"
                f"?semester={semester.name}"
                f"&year={semester.year_gap}"
            )

            async with self.__session.get(endpoint) as response:
                if isinstance((data := await response.json()), dict):
                    return [
                        PaveStudent(self.__client, raw_data)
                        for raw_data in data.get("rows", [])
                    ]

                raise ImproperApiResultException()

        for s in (
            self.__client.semesters or await self.__client.fetch_semesters()
        ):
            mines: list[PaveStudent] = []

            endpoint = (
                f"{API_URL}"
                "/extranet/student/queries/paves/student-paves"
                f"?semester={s.name}"
                f"&year={s.year_gap}"
            )

            async with self.__session.get(endpoint) as response:
                if response.status != 200:
                    continue

                if isinstance((data := await response.json()), dict):
                    mines.extend(
                        PaveStudent(self.__client, raw_data)
                        for raw_data in data.get("rows", [])
                    )
                else:
                    raise ImproperApiResultException()

            self.__mines = mines

        return self.mines or []
