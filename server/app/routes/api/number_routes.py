import os
import logging
from flask import request, jsonify

from app.services.number import Numerator

logger = logging.getLogger('HELLO WORLD')

def number_route(app):
    @app.route('/upload/number', methods=['POST'])
    def number():
        identifier = request.form['id']
        filename = identifier
        Numerator(filename).run()
        pathFile = f"http://localhost:5000/uploads/output/number/{identifier}.png"
        return jsonify({"image": pathFile})