import os
from werkzeug.utils import secure_filename
from flask import current_app as app

def handle_image_upload(file):
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['MEDIA_FOLDER'], filename)
        file.save(file_path)
        return filename
    return None

def delete_image(filename):
    if filename:
        file_path = os.path.join(app.config['MEDIA_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)