import os
from flask import render_template, request, url_for, send_from_directory, current_app, jsonify
from werkzeug.utils import secure_filename
from app.admin import admin_bp
from flask_login import login_required
from utils.decorators import admin_required

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')