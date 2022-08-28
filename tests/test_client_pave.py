import asyncio
import os

import pytest

from myefrei_sdk.client import Client


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_pave_associations(
    event_loop: asyncio.BaseEventLoop,
) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    assert not client.pave.associations

    associations = await client.pave.fetch_associations()

    assert associations
    assert client.pave.associations == associations

    await client.disconnect()


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_pave_roles(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    assert not client.pave.roles

    roles = await client.pave.fetch_roles()

    assert roles
    assert client.pave.roles == roles

    await client.disconnect()


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_pave_interests(
    event_loop: asyncio.BaseEventLoop,
) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    assert not client.pave.interests

    interests = await client.pave.fetch_interests()

    assert interests
    assert client.pave.interests == interests

    await client.disconnect()


@pytest.mark.asyncio  # type: ignore[misc]
async def test_client_pave_mines(event_loop: asyncio.BaseEventLoop) -> None:
    client = Client(os.environ["SID"], loop=event_loop)

    await client.connect()

    mines = await client.pave.fetch_mines()

    assert mines
    assert client.pave.mines == mines

    await client.disconnect()
