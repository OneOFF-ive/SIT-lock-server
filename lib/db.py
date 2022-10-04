import asyncio
import aiomysql

from lib.config import DatabaseConfig
from lib.util import JsonDecodeToConfig


class Database:
    def __init__(self):
        self.__pool = None

    async def pool_init(self, config: DatabaseConfig, minsize, maxsize, autocommit):
        await self.__pool_init(config, minsize, maxsize, autocommit)

    async def __pool_init(self, config: DatabaseConfig, minsize, maxsize, autocommit):
        self.__pool = await aiomysql.create_pool(
            minsize=minsize,  # 连接池最小值
            maxsize=maxsize,  # 连接池最大值
            host=config.host,
            port=config.port,
            user=config.username,
            password=config.password,
            db=config.db,
            autocommit=autocommit,  # 自动提交模式
        )

    async def __getCursor(self):
        conn = await self.__pool.acquire()
        # 返回字典格式
        cur = await conn.cursor(aiomysql.DictCursor)
        return conn, cur

    async def __closeCursor(self, conn, cur):
        if cur:
            await cur.close()
        # 释放掉conn,将连接放回到连接池中
        await self.__pool.release(conn)

    async def query(self, query, param=None):
        """
        查询操作
        :param query: sql语句
        :param param: 参数
        :return:
        """
        conn, cur = await self.__getCursor()
        await cur.execute(query, param)
        res = await cur.fetchall()

        await self.__closeCursor(conn, cur)
        return res

    async def execute(self, query, param=None):
        """
        增删改 操作
        :param query: sql语句
        :param param: 参数
        :return:
        """
        conn, cur = await self.__getCursor()
        res = True

        await cur.execute(query, param)
        if cur.rowcount == 0:
            res = False
        await self.__closeCursor(conn, cur)
        return res


class DatabaseBuilder:

    async def build(config: DatabaseConfig, minsize=2, maxsize=5, autocommit=True):
        db = Database()
        await db.pool_init(config, minsize, maxsize, autocommit)
        return db


async def setDatabase(app):
    app['db'] = await DatabaseBuilder.build(app['config'].database)
