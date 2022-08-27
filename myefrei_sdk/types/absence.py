import datetime
import typing


ExcusedAbsence = typing.Literal["Excusée", "Non excusée"]
AbsenceCode = typing.Literal["ABS", "ABS-EXCUSE"]


class Absence(typing.TypedDict):
    act_cod_description: str
    soff_offering_desc: str

    cust_semester: str
    soff_academic_per_id: str

    soff_service_offering_id: str

    student_absence_code_absence: AbsenceCode
    student_absence_class_date: datetime.datetime
    student_absence_description: str
    student_absence_excused: ExcusedAbsence

    time_cr_abs_hours: float
    time_cr_block_id: str
    time_cr_time_from: str

    student_number: int
