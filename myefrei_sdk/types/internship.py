"""
https://www.myefrei.fr/api/extranet/student/queries/internships

return:
    {
        "rows": [
            {
                "custFirmContact": "",
                "epsProgramOffId": "",
                "internshipDateFrom": "",
                "internshipDateTo": "",
                "internshipId": "",
                "internshipPk": "",
                "internshipSubject": "",
                "internshipProposalStage": "",
                "stdNumber": "",
                "stdPk": ""
            },
            ...
        ],
        "totalRowCount": 0
    }

"""
import datetime
import typing


PROPOSAL = typing.Literal["INITIE", "ACCEPTE"]


class Internship(typing.TypedDict):
    custFirmContact: str

    epsProgramOffId: str

    internship_date_from: datetime.datetime
    internship_date_to: datetime.datetime

    internship_id: str
    internship_pk: int

    internship_subject: str
    internship_proposal_stage: PROPOSAL

    student_number: int
    student_pk: int
