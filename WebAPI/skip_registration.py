from aiohttp import web
from lib.lock_url_builder import *
from lib.send_request import *


async def skip_registration(request):
    url = await build_shuaka_liu_cheng_url_by_config(request.app['config'].lock)
    await send_request(url)
    return web.Response(text='skip')
