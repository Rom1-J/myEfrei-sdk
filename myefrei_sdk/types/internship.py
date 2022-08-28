import typing


INTERNSHIP_STATE = typing.Literal["INITIE", "ACCEPTE"]


class Internship(typing.TypedDict):
    custFirmContact: str
    epsProgramOffId: str
    internshipDateFrom: str
    internshipDateTo: str
    internshipId: str
    internshipPk: str
    internshipSubject: str
    internshipProposalStage: INTERNSHIP_STATE
    stdNumber: str
    stdPk: str
