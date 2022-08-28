import asyncio
import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_semesters(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    assert not client.semesters

    semesters = await client.fetch_semesters()

    assert semesters
    assert client.semesters == semesters

    await client.disconnect()


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_semester_absences(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    await client.fetch_semesters()
    semester = client.get_semester("S6")

    assert semester
    assert isinstance(await semester.fetch_absences(), list)

    await client.disconnect()
