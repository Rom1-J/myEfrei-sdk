import asyncio
import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_connect(event_loop: asyncio.BaseEventLoop) -> None:
    async with Client(os.environ["SID"], loop=event_loop) as client:
        assert client.user
