import logging
import os
from circulo import Circle
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
    inputFolder = os.path.join(app.config['UPLOAD_FOLDER'], 'input')
    outputFolder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
    if not os.path.isdir(inputFolder):
        os.mkdir(inputFolder)
    logger.info("welcome to upload`")
    file = request.files['file']
    filename = secure_filename(file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        print(file_ext)
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
    destination = "/".join([inputFolder, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    Circle(filename).run()

    full_filename = "http://localhost:5000/uploads/output/result-canvas-notnumber.png"
    print(full_filename)
    time.sleep(10)
    return jsonify({"image": full_filename})


@app.route('/uploads/output/<filename>')
def send_file(filename):
    inputFolder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
    return send_from_directory(inputFolder, filename)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=5000)
