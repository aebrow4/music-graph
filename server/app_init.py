from flask import Flask
from flask_rebar import Rebar

from server.rebar import rebar
from server.register_handlers import register_handlers
from graph.db import get_driver, init_neomodel_client
from config.base import get_config

def _init_db(app):
    app.app_ctx_globals_class.driver = get_driver()
    init_neomodel_client()

def _register_handlers():
    register_handlers()

def create_app(config=get_config()):
    app = Flask(__name__)
    _register_handlers()
    rebar.init_app(app)
    app.config.update(config)

    _init_db(app)
    return app
