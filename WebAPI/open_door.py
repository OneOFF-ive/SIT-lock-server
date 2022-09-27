import asyncio
from WebAPI.lib.lock_url_builder import *
from WebAPI.lib.send_request import *
from WebAPI.lib.default_config import *


async def open_door():
    url = await build_remote_open_door_url_by_config(default_config.lock)
    await send_request(url)

loop = asyncio.get_event_loop()
loop.run_until_complete(open_door())
