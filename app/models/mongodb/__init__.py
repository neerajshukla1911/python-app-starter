import asyncio
import motor.motor_asyncio
loop = asyncio.get_event_loop()


motor_client = motor.motor_asyncio.AsyncIOMotorClient(io_loop=loop)