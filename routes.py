from views import index
from WebAPI.open_door import open_door
from WebAPI.skip_registration import skip_registration


def setup_routes(app):
    app.router.add_get('/open_door', open_door)
    app.router.add_get('/skip_reg', skip_registration)
    app.router.add_get('/', index)
