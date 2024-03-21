import os
import logging
from flask import Flask, render_template
from flask_cors import CORS
from flask_docs import ApiDoc

from app.routes import register_routes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Define allowed file extensions for file uploads
app.config['UPLOAD_EXTENSIONS'] = ['.png', '.jpg', '.jpeg']

CORS(app, expose_headers='Authorization')

# Ensure that input and output folders exist
input_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'input')
output_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Register your routes
register_routes(app)

# Initialize Flask-Docs
ApiDoc(
    app,
    title="Circlism App",
    version="1.0.0",
    description="The Circlism API",
)

# Enable auto-generating args.md
app.config["API_DOC_AUTO_GENERATING_ARGS_MD"] = True

#@app.errorhandler(404)
#def not_found(e):
#    return render_template("index.html")

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000, use_reloader=True)
