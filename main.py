from aiohttp import web
from routes import setup_routes
from lib.default_config import default_config
from lib.db import setDatabase, closeDatabase

app = web.Application()
app['config'] = default_config
app.on_startup.append(setDatabase)
app.on_cleanup.append(closeDatabase)
setup_routes(app)
web.run_app(app, host='0.0.0.0', port=8081)


