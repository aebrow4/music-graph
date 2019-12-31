from flask import Flask
from flask_rebar import Rebar

rebar = Rebar()
registry = rebar.create_handler_registry()

