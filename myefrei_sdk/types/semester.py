import typing


class Semester(typing.TypedDict):
    cust_current_semester: bool
    cust_semester: str
    cust_year_id: int
    soff_academic_per_id: str
    student_number: int
