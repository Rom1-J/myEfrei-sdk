import asyncio
import datetime
import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_rooms(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    date = datetime.datetime(year=2022, month=4, day=14)
    rooms = await client.fetch_rooms(date)

    assert rooms

    await client.disconnect()

