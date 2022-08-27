"""
https://www.myefrei.fr/api/extranet/student/queries/student-courses-semester

args:
    semester: (ex. S6)
    year: yyyy-yyyy

return:
    {
        "rows": [
            {
                "custActualMkState": "",
                "custApproved": "",
                "custExamination": "",
                "custMarkCode": "",
                "level1Name": "",
                "level2Name": "",
                "level3Name": "",
                "custSemester": "",
                "soffAcadPerId": "",
                "soffCredits": "",
                "soffCreditsAttempt": "",
                "soffCreditsEarned": "",
                "soffOfferingDesc": "",
                "soffServiceGrpId": "",
                "soffServiceoffPk": "",
                "soffliParentServoffFk": "",
                "stdNumber": ""
            },
            ...
        ],
        "totalRowCount": 0
    }



https://www.myefrei.fr/api/extranet/student/queries/planning?enddate=2022-09-12&startdate=2022-08-01

args:
    startdate:  yyyy-mm-dd
    enddate: yyyy-mm-dd

return:
    {
        "rows": [
            {
                "tchResName": "",
                "client": "",
                "custTypeSeance": "",
                "prgoOfferingDesc": "",
                "soffDeliveryMode": "",
                "soffServiceId": "",
                "soffServiceOffId": "",
                "srvTimeCrActivityId": "",
                "srvTimeCrDateFrom": "",
                "srvTimeCrDelRoom": "",
                "stdNumber": "",
                "stdPk": "",
                "timeCrTimeFrom": "",
                "timeCrTimeTo": "",
                "valDescription": ""
            },
            ...
        ],
        "totalRowCount": 0
    }


"""
import datetime
import typing


GROUP_ID = typing.Literal["MODULE", "FFPNOTE", "EXAMEN"]


class Course(typing.TypedDict):
    cust_actual_mark_state: str
    cust_approved: bool
    cust_examination: str | None
    cust_mark_code: str | None
    cust_semester: str

    level1_name: str | None
    level2_name: str | None
    level3_name: str | None

    soff_academic_per_id: str

    soff_credits: float
    soff_credits_attempt: int | None
    soff_credits_earned: int

    soff_offering_description: str

    soff_service_group_id: GROUP_ID
    soff_service_offering_pk: int

    soff_li_parent_service_offering__fk: int

    student_number: int


class ScheduledCourse(typing.TypedDict):
    teacher_responsable_name: str
    client: str

    cust_type_seance: int

    prgo_offering_description: str

    soff_delivery_mode: str
    soff_service_id: str
    soff_service_offering_id: str

    srv_time_cr_activity_id: str
    srv_time_cr_date_from: datetime.datetime
    srv_time_cr_del_room: str

    time_cr_time_from: str
    time_cr_time_to: str

    val_description: str

    student_number: int
    student_pk: int
