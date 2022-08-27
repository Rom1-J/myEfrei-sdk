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
    id: int
    name: str


class Role(typing.TypedDict):
    id: int
    name: ROLE


class Interest(typing.TypedDict):
    id: int
    time: TIME


class Pave(typing.TypedDict):
    id: int
    association_id: int
    association_name: str

    role_id: int
    role_name: str
    other_role: str | None
    invested_time: str

    mission: str
    acquired_skills: str
    motivation: str

    mark: int
    public_comment: str | None
    pave_period_id: int
