import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Models.User import User
from core.database_config import SessionLocal

fedya = User(username='fedya2001', is_artist=False, password_hash='fjidgbwsfew', avatar_url='fedya.png')

import asyncio

async def LoadDataToTable(obj):
    try:
        async with SessionLocal() as session:
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            print('Y')
            return True
    except Exception as e:
        print('N')
        if session:
            await session.rollback()
        return False

asyncio.run(LoadDataToTable(fedya))


