import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio
async def test_client_semesters() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert not client.semesters

    semesters = await client.fetch_semesters()

    assert semesters
    assert client.semesters == semesters
