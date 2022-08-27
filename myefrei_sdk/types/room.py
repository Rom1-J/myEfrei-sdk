"""
https://www.myefrei.fr/api/extranet/queries/free-rooms

args:
    date: yyyy-mm-dd

return:
    {
        "rows": [
            {
                "id": "",
                "st": "",
                "rn": "",
                "rt": "",
                "sn": ""
            },
            ...
        ],
        "totalRowCount": 0
    }

"""
import typing


class Room(typing.TypedDict):
    time: str
    room_name: str
    room_type: str
    site_name: str
