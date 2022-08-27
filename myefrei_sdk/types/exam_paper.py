"""
https://www.myefrei.fr/api/extranet/student/queries/dms/exam-papers

return:
    {
        "rows": [
            {
                "createDate": "",
                "fileName": "",
                "username": "",
                "stdFullName": "",
                "examDate": "",
                "examType": "",
                "courseCode": "",
                "courseName": "",
                "teachers": []
            },
            ...
        ],
        "totalRowCount": 0
    }

"""
import datetime
import typing


EXAM_TYPE = typing.Literal["DE", "CE", "RAT"]


class ExamPaper(typing.TypedDict):
    create_date: datetime.datetime
    exam_date: datetime.datetime

    file_name: str
    exam_type: EXAM_TYPE

    course_name: str
    course_code: str
    teachers: list[str] | None

    std_full_name: str
    username: str
