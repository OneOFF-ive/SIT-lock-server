import aiomysql
from lib.config import DatabaseConfig


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
            pool_recycle=300,       # 连接池刷新
        )

    async def __getCursor(self):
        conn = await self.__pool.acquire()

        # 测试连接是否过期
        while True:
            try:
                conn.ping()
                break
            except aiomysql.OperationalError:
                conn.ping(True)

        # 返回字典格式
        cur = await conn.cursor(aiomysql.DictCursor)
        return conn, cur

    async def __closeCursor(self, conn, cur):
        if cur:
            await cur.close()
        # 释放掉conn,将连接放回到连接池中
        await self.__pool.release(conn)

    async def query(self, sql: str, param: tuple = None):
        """
        查询操作
        :param sql: sql语句
        :param param: 参数
        :return:
        """
        conn, cur = await self.__getCursor()
        await cur.execute(sql, param)
        res = await cur.fetchall()

        await self.__closeCursor(conn, cur)
        return res

    async def execute(self, sql: str, param: tuple = None):
        """
        增删改 操作
        :param sql: sql语句
        :param param: 参数
        :return:
        """
        conn, cur = await self.__getCursor()
        res = True

        await cur.execute(sql, param)
        if cur.rowcount == 0:
            res = False
        await self.__closeCursor(conn, cur)
        return res

    async def close(self):
        self.__pool.close()
        await self.__pool.wait_closed()


class DatabaseBuilder:
    async def build(config: DatabaseConfig, minsize=2, maxsize=5, autocommit=True):
        db = Database()
        await db.pool_init(config, minsize, maxsize, autocommit)
        return db


async def setDatabase(app):
    app['db'] = await DatabaseBuilder.build(app['config'].database)


async def closeDatabase(app):
    await app['db'].close()


__all__ = [
    "Database",
    "DatabaseBuilder",
    "setDatabase",
    "closeDatabase",
]