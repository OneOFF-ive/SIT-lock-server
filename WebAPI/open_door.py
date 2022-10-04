import asyncio

from aiohttp import web
from lib.lock_url_builder import *
from lib.send_request import *


async def open_door(request):

    url = await build_remote_open_door_url_by_config(request.app['config'].lock)
    # await send_request(url)
    asyncio.create_task(send_request(url))
    return web.Response(text='open')

