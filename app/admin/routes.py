import os

from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from . import admin, admin_bp


@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')
@admin_bp.route('/accounts')
def accounts():
    return render_template('admin/accounts.html')
@admin_bp.route('/posts')
def posts():
    return render_template('admin/posts.html')
@admin_bp.route('/posts/add-new')
def add_new_posts():
    return render_template('admin/add-posts.html')