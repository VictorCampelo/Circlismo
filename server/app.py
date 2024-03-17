import logging
import os
from circulo import Circle
from numerator import Numerator
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


@app.route('/upload/ciclism', methods=['POST'])
def circlism():
    input_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'input')
    output_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
    
    # Ensure that input and output folders exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    logger.info("Welcome to upload")
    file = request.files['file']
    identifier = request.form['id']
    logger.info(f"Processing file with ID: {identifier}")

    filename = secure_filename(file.filename)
    
    # Check if the filename is not empty
    if filename == '':
        abort(400)

    # Check the file extension
    file_ext = os.path.splitext(filename)[1]
    if file_ext not in app.config['UPLOAD_EXTENSIONS']:
        abort(400)
        
    filename = identifier + '.png'
    
    # Save the file to the input folder
    destination = os.path.join(input_folder, filename)
    file.save(destination)
    session['uploadFilePath'] = destination

    # Run Circle algorithm on the uploaded image
    Circle(filename).run()

    # URL for the output image
    full_filename = f"http://localhost:5000/uploads/output/{identifier}.svg"
    
    # Delay the response to ensure the processing is completed
    time.sleep(10)
    
    # Return the URL of the processed image
    return jsonify({"image": full_filename})

@app.route('/upload/number', methods=['POST'])
def number():
    identifier = request.form['id']
    filename = identifier
    Numerator(filename).run()
    pathFile = f"http://localhost:5000/uploads/output/number/{identifier}.png"
    return jsonify({"image": pathFile})

@app.route('/uploads/output/<filename>')
def send_file(filename):
    inputFolder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
    return send_from_directory(inputFolder, filename)

@app.route('/uploads/output/number/<filename>')
def send_file_number(filename):
    inputFolder = os.path.join(app.config['UPLOAD_FOLDER'], 'output', 'number')
    return send_from_directory(inputFolder, filename)

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=5000)
