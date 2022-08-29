import asyncio
import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_courses(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    assert not client.courses

    await client.fetch_semesters()
    semester = client.get_semester("s5")

    courses = await client.fetch_courses(semester)

    assert courses
    assert client.courses == courses

    await client.disconnect()
