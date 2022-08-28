import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_notification() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert not client.documents

    documents = await client.fetch_documents()

    assert documents
    assert client.documents == documents
