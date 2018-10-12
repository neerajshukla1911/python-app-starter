from sanic import Sanic
from config_reader import get_config
from log_config import get_log_config

config = get_config('sanic_app')


def configure():
    sanic_app.config.update(config)

    from sanic_app.api.v1 import api_v1
    sanic_app.blueprint(api_v1, url_prefix='/api/v1')


sanic_app = Sanic(log_config=get_log_config())
configure()
