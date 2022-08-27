"""
https://www.myefrei.fr/user

return:
    [
        {
            "sub": "",
            "username": "",
            "firstname": "",
            "name": "",
            "fullname": "",
            "email": "",
            "email_verified": "",
            "role": "",
            "home": "",
            "authorities": [
                {
                    "authority": ""
                },
                ...
            ],
        },
        ...
    ]



https://www.myefrei.fr/api/extranet/student/queries/student-documents

return:
    {
        "rows": [
            {
                "docType": "",
                "docFreeText": "",
                "docMimeType": "",
                "docSequenceNo": "",
                "docStatus": "",
                "docTitle": "",
                "docBlobFileGuid": "",
                "docBlobFileSize": "",
                "docPageGuid": "",
                "docPageLastUpdate": "",
                "docPageRevNo": "",
                "docTypeName": "",
                "stdNumber": ""
            },
            ...
        ],
        "totalRowCount": 0
    }

"""
import datetime
import typing
import uuid


AUTHORITY_TYPE = typing.Literal[
    "ROLE_USER",
    "ROLE_STUDENT",
    "EXTRANET",
    "PORTAL",
    "API",
    "STUDAPART",
    "STUDEAL",
    "APPSCHO",
    "JOBTEASER",
]
DOCUMENT_TYPE = typing.Literal["DOCADMIN", "RESULTS.ACAD"]


class UserAuthority(typing.TypedDict):
    authority: AUTHORITY_TYPE


class User(typing.TypedDict):
    authorities: list[UserAuthority]

    email: str
    email_verified: bool

    firstname: str
    name: str
    fullname: str
    username: str
    sub: int

    home: str
    role: str


class Document(typing.TypedDict):
    document_type: DOCUMENT_TYPE
    document_free_text: str | None
    document_mime_type: str
    document_sequence_no: int
    document_status: str
    document_title: str
    document_blob_file_guid: str
    document_blob_file_size: int
    document_page_guid: uuid.UUID
    document_Page_last_update: datetime.datetime
    document_Page_revision_no: int
    document_Type_name: str

    student_number: int
