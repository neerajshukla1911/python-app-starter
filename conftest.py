import asyncio
import pytest

@pytest.yield_fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()