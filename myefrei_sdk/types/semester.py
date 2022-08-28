import typing


class Semester(typing.TypedDict):
    custSemester: str
    custYearId: str
    soffAcadPerId: str
    stdNumber: str
    custCurrentSemester: bool | None
