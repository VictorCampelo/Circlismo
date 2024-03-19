import os
import logging
from flask import send_from_directory

def get_files_route(app):
    @app.route('/uploads/output/<filename>')
    def send_file(filename):
        inputFolder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
        return send_from_directory(inputFolder, filename)

    @app.route('/uploads/output/number/<filename>')
    def send_file_number(filename):
        inputFolder = os.path.join(app.config['UPLOAD_FOLDER'], 'output', 'number')
        identifier = os.path.splitext(filename)[0]
        # delete_files_with_identifier(identifier)
        return send_from_directory(inputFolder, filename)
    
    def delete_files_with_identifier(identifier):
        upload_folder = os.path.join(app.config['UPLOAD_FOLDER'])
        for root, dirs, files in os.walk(upload_folder):
            for file_name in files:
                if identifier in file_name:
                    file_path = os.path.join(root, file_name)
                    os.remove(file_path)