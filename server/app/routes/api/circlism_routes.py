# circlism_routes.py

import os
import time
import logging
from flask import abort, request, session, jsonify
from werkzeug.utils import secure_filename

from app.services.circlism import Circle

logger = logging.getLogger('HELLO WORLD')

ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg'])

def circlism_route(app):
    @app.route('/upload/ciclism', methods=['POST'])
    def circlism():
        """Upload and process images using the circlism algorithm.

        @@@
        ### description
        > Upload and process images using the circlism algorithm.

        ### args
        |  args       | required | request type | type |  remarks       |
        |-------------|----------|--------------|------|----------------|
        |  file       |  true    |    form-data | file | image file     |
        |  id         |  true    |    form-data | str  | image ID       |

        ### request
        ```json
        {"name": "xx", "type": "code"}
        ```

        ### return
        ```json
        {"image": "http://localhost:5000/uploads/output/{identifier}.svg"}
        ```
        @@@
        """
        
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
