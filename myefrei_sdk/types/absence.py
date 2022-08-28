import typing


ExcusedAbsence = typing.Literal["Excusée", "Non excusée"]
AbsenceCode = typing.Literal["ABS", "ABS-EXCUSE"]


class Absence(typing.TypedDict):
    actCodDescription: str
    custSemester: str
    soffAcadPerId: str
    soffOfferingDesc: str
    soffServiceOffId: str
    stdNumber: str
    stdAbsCodeAbsence: AbsenceCode
    stdAbsClassDate: str
    stdAbsDescription: str
    stdAbsExcused: ExcusedAbsence
    timeCrAbsHours: str
    timeCrBlockId: str
    timeCrTimeFrom: str
