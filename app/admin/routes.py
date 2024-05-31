import os

from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from . import admin

@admin.route('/admin/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')
@admin.route('/admin/accounts')
def accounts():
    return render_template('admin/accounts.html')
@admin.route('/admin/posts')
def posts():
    return render_template('admin/posts.html')
@admin.route('/admin/posts/add-new')
def add_new_posts():
    return render_template('admin/add-posts.html')