from aiohttp import web
from routes import setup_routes
from lib.default_config import default_config
from lib.db import setDatabase


async def main():
    app = web.Application()
    app['config'] = default_config
    await setDatabase(app)
    setup_routes(app)
    web.run_app(app, host='0.0.0.0', port=8080)
