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
