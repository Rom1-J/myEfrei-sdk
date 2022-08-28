import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_semesters() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert not client.semesters

    semesters = await client.fetch_semesters()

    assert semesters
    assert client.semesters == semesters


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_semester_absences() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    await client.fetch_semesters()
    semester = client.get_semester("S6")

    assert semester
    assert isinstance(await semester.fetch_absences(), list)
