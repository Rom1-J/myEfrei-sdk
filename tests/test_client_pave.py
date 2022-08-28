import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio
async def test_client_pave_associations() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert not client.pave.associations

    associations = await client.pave.fetch_associations()

    assert associations
    assert client.pave.associations == associations


@pytest.mark.asyncio
async def test_client_pave_roles() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert not client.pave.roles

    roles = await client.pave.fetch_roles()

    assert roles
    assert client.pave.roles == roles


@pytest.mark.asyncio
async def test_client_pave_interests() -> None:
    client = Client()

    await client.connect(os.environ["SID"])

    assert not client.pave.interests

    interests = await client.pave.fetch_interests()

    assert interests
    assert client.pave.interests == interests


@pytest.mark.asyncio
async def test_client_pave_mines() -> None:
    client = Client()

    await client.connect(os.environ["SID"], fetch_all=True)

    mines = await client.pave.fetch_mines()

    assert mines
    assert client.pave.mines == mines
