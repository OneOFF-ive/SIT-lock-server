import json
import aiohttp
from lib.config import *
from lib.db import Database


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


def JsonDecodeToConfig(file_name: str):
    with open(file_name) as fp:
        config_dict = json.load(fp=fp)
        return Config(database=DatabaseConfig(**config_dict.get("database")),
                      lock=LockConfig(**config_dict.get("lock")))


async def send_request(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # print(resp.status)
            return await resp.text()


async def check_user_by_id(db: Database, s_id: str):
    sql = 'select * from user where s_id = %s'
    values = (s_id,)
    return await db.query(sql, values)


async def check_user_by_no(db: Database, c_no: str):
    sql = 'select * from user where c_no = %s'
    values = (c_no,)
    return await db.query(sql, values)


# 指明util模块中需要导出的对象
__all__ = [
    "Singleton",
    "JsonDecodeToConfig",
    "send_request",
    "check_user_by_id",
    "check_user_by_no"
]
