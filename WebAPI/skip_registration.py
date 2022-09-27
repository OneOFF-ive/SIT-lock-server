import asyncio
from WebAPI.lib.lock_url_builder import *
from WebAPI.lib.send_request import *
from WebAPI.lib.default_config import *


async def main():
    url = await build_shuaka_liu_cheng_url_by_config(default_config.lock)
    await send_request(url)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
