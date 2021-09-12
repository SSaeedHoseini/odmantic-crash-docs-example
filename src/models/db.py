import sys

from motor.motor_asyncio import AsyncIOMotorClient

from odmantic import AIOEngine


def get_db():
    motor = AsyncIOMotorClient()
    if "pytest" in sys.modules:
        return AIOEngine(motor_client=motor, database="CircularErrorTest")
    return AIOEngine(motor_client=motor, database="CircularError")
