from aiohttp import web
from WebAPI.lib.lock_url_builder import *
from WebAPI.lib.send_request import *
from WebAPI.lib.default_config import *


async def open_door(response):
    url = await build_remote_open_door_url_by_config(default_config.lock)
    await send_request(url)
    return web.Response(text='open')

