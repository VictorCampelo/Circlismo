# __init__.py inside the routes package

from flask import Flask

from app.routes.api.circlism_routes import circlism_route
from app.routes.api.number_routes import number_route
from app.routes.api.get_files_routes import get_files_route

def register_routes(app: Flask):
    circlism_route(app)
    number_route(app)
    get_files_route(app)
