import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_connect() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert client.user
