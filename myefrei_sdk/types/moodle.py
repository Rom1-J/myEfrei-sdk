import typing


GROUP_ID = typing.Literal["FFPNONNOTE", "FFPNOTE", "EXAMEN"]


class MoodleIdentifier(typing.TypedDict):
    compute_id: str
    name_module: str


class Moodle(typing.TypedDict):
    level1_name: str | None
    level2_name: str | None
    level3_name: str | None

    cust_aggregate_name: str | None
    cust_semester: str

    cust_moodle_identifier: list[MoodleIdentifier] | None

    enr_service_id: str
    enr_service_offering_id: str

    courses_space: bool

    soff_academic_per_id: str
    soff_delivery_mode: str
    soff_offering_description: str

    soff_service_group_id: GROUP_ID
    soff_service_offering_pk: int

    soff_li_parent_service_offering_fk: int

    student_number: int
