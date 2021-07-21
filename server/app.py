import logging
import os
import time

from flask import Flask, abort, request, send_from_directory, session, render_template, make_response, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')

ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg'])

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['UPLOAD_EXTENSIONS'] = ALLOWED_EXTENSIONS

CORS(app, expose_headers='Authorization')


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(app.config['UPLOAD_FOLDER'], 'input')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file']
    filename = secure_filename(file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        print(file_ext)
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    full_filename = "http://localhost:8000/uploads/test/" + filename
    print(full_filename)
    time.sleep(10)
    return jsonify({"image": full_filename})


@app.route('/uploads/test/<filename>')
def send_file(filename):
    target = os.path.join(app.config['UPLOAD_FOLDER'], 'test')
    return send_from_directory(target, filename)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8000)
