import typing


ROLE = typing.Literal[
    "Président",
    "Trésorier",
    "Secrétaire",
    "Vice-président",
    "Responsable de projet",
    "Responsable communication",
    "Responsable partenariats",
    "Organisateur d'événements",
    "Animateur d'événements",
    "Formateur",
    "Membre d'équipe de spectacle publics",
    "Membre d'équipe de compétition",
    "Autre",
]
TIME = typing.Literal[
    "Moins de 5h",
    "Entre 5h et 10h",
    "Entre 10h et 15h",
    "Entre 15h et 20h",
    "Entre 20h et 30h",
    "Plus de 30h",
]


class Association(typing.TypedDict):
    id: str
    name: str


class Role(typing.TypedDict):
    id: str
    name: ROLE


class Interest(typing.TypedDict):
    id: str
    time: TIME


class Pave(typing.TypedDict):
    id: int
    associationId: int
    associationName: str
    roleId: int
    roleName: ROLE
    otherRole: str
    investedTime: TIME
    mission: str
    acquiredSkills: str
    motivation: str
    mark: int
    publicComment: str | None
    pavePeriodId: int
