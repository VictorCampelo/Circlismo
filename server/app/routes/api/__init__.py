from flask import Blueprint

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__)

# Import API route modules to register routes with the Blueprint
from . import circlism_routes, number_routes