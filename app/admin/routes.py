import os
from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
from . import admin_bp
from app.models.posts import Post
from app.models.categories import Category

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/accounts')
def accounts():
    return render_template('admin/accounts.html')

@admin_bp.route('/posts')
def posts():
    # Lấy tất cả các chuyên mục từ database
    all_cat = Category.query.all()
    # Lấy tất cả các bài viết từ database
    all_posts = Post.query.all()
    return render_template('admin/posts.html', categories = all_cat, posts=all_posts)

@admin_bp.route('/posts/add-new')
def add_new_posts():
    return render_template('admin/add-posts.html')