from flask import Flask

from graph.db import get_driver
from config.base import get_config
from server.register_handlers import register_handlers


def _init_db(app):
    app.app_ctx_globals_class.driver = get_driver()


def _register_handlers(app):
    register_handlers(app)


def create_app(config=get_config()):
    app = Flask(__name__)
    app.config.update(config)

    _register_handlers(app)
    _init_db(app)
    return app
