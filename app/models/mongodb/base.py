from app import config
from app.models.mongodb import motor_client
from uuid import uuid4


class BaseDocument(object):

    def __init__(self):
        self.db = motor_client[config['mongodb']['name']]
        self.name = 'base'

    def _generate_id(self):
        return str(uuid4())

    def find_one(self, filter=None, *args, **kwargs):
        return self.db[self.name].find_one(filter)

    def find(self, filter, *args, **kwargs):
        return self.db[self.name].find(filter)

    async def insert_one(self, document, *args, **kwargs):
        document['_id'] = self._generate_id()
        fut = await self.db[self.name].insert_one(document)
        return fut

    async def insert_many(self, filter, *args, **kwargs):
        pass

    async def update_one(self, filter, *args, **kwargs):
        pass

    async def update_many(self, filter, *args, **kwargs):
        pass

    async def delete_one(self, filter, *args, **kwargs):
        pass

    async def delete_many(self, filter, *args, **kwargs):
        fut = await self.db[self.name].delete_many(filter)
        return fut
