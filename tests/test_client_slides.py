import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_slides() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert not client.slides

    slides = await client.fetch_slides()

    assert slides
    assert client.slides == slides


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_slide() -> None:
    client = Client()

    await client.connect(os.environ["SID"])
    slides = await client.fetch_slides()

    assert await client.fetch_slide(slides[0].token)
