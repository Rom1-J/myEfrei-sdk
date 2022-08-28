import asyncio
import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_slides(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    assert not client.slides

    slides = await client.fetch_slides()

    assert slides
    assert client.slides == slides

    await client.disconnect()


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_slide(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()
    slides = await client.fetch_slides()

    assert await client.fetch_slide(slides[0].token)

    await client.disconnect()
