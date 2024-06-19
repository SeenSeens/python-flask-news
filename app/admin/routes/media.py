import os
from flask import request, url_for, send_from_directory, current_app, jsonify
from werkzeug.utils import secure_filename
from app.admin import admin_bp
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin_bp.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['MEDIA_FOLDER'], filename))
        return jsonify({'location': url_for('media', filename=filename, _external=True)})
    return jsonify({'error': 'File type not allowed'}), 400

@admin_bp.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config['MEDIA_FOLDER'], filename)