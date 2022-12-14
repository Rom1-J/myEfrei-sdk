import asyncio
import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_connect(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    assert client.user

    await client.disconnect()
