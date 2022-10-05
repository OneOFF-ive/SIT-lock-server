from aiohttp import web
from lib.lock_url_builder import build_shuaka_liu_cheng_url_by_config
from lib.util import send_request, check_user_by_no
from lib.db import Database


async def skip_registration(request):
    db: Database = request.app['db']
    text: str = "卡未注册"

    params = dict(request.query)
    userList: tuple = ()
    if 'c_no' in params and params['c_no']:
        userList = await check_user_by_no(db, params['c_no'])

    if userList:
        url = await build_shuaka_liu_cheng_url_by_config(request.app['config'].lock)
        await send_request(url)
        text = userList[0]['name'] + ",开门成功"

    return web.Response(
        text=text)
