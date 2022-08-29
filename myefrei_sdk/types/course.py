import datetime
import typing


if typing.TYPE_CHECKING:
    from .teacher import Teacher


SERVICE_GROUP_ID = typing.Literal[
    "RATTRAPAGE",
    "UE",
    "EXAMEN",
    "FFPNONNOTE",
    "FFPNOTE",
    "MODULE",
    "NOTESEULE",
]


class ModuleIdentifier(typing.TypedDict):
    computeId: str
    nameModule: str


class ScheduledCourse(typing.TypedDict):
    pk: int

    teacher: list["Teacher"]

    room: str
    activity: str

    description: str
    category: str

    date: datetime.datetime
    start: datetime.datetime
    end: datetime.datetime


class Course(typing.TypedDict):
    level1Name: str
    level2Name: str
    level3Name: str
    custAggregateName: str
    custSemester: str
    enrServiceId: str
    enrServiceoffId: str
    coursesSpace: str
    soffAcadPerId: str
    soffDeliveryMode: str
    soffOfferingDesc: str
    soffServiceGrpId: SERVICE_GROUP_ID
    soffServiceoffPk: str
    soffliParentServoffFk: str
    stdNumber: str
    custMoodleIdentifier: list[ModuleIdentifier]
