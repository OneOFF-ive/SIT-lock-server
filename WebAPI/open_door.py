from lib.db import Database
from aiohttp import web
from lib.lock_url_builder import *
from lib.util import send_request, check_user_by_id, check_user_by_no


async def open_door(request):
    db: Database = request.app['db']
    text: str = '0'

    params = dict(request.query)
    userList: tuple = ()
    if 's_id' in params and params['s_id']:
        userList = await check_user_by_id(db, params['s_id'])
    elif 'c_no' in params and params['c_no']:
        userList = await check_user_by_no(db, params['c_no'])

    if userList:
        url = await build_remote_open_door_url_by_config(request.app['config'].lock)
        res = await send_request(url)
        text: str = '1'

    return web.Response(
            text=text)

