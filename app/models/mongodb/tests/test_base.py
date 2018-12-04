import pytest
from app.models.mongodb.base import BaseDocument


@pytest.mark.asyncio
async def test_insert_one():
    await BaseDocument().delete_many({})
    await BaseDocument().insert_one({'name': 'insert_one'})
    cursor = BaseDocument().find({})
    data = await cursor.to_list(20)
    assert len(data) == 1, "length is {}".format(len(data))
