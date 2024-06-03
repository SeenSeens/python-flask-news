import os
from flask import render_template, request, redirect, url_for, Blueprint, flash, jsonify
from werkzeug.utils import secure_filename
from . import admin_bp
from app.models.posts import Post
from app.models.categories import Category
from app import db

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

@admin_bp.route('/post/add-new', methods=['GET', 'POST'])
def add_new_posts():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        # excerpt = request.form['excerpt']
        # thumbnail = request.form['thumbnail']
        category_id = request.form['category_id']

        new_post = Post(
            name=name,
            description=description,
            # excerpt=excerpt,
            # thumbnail=thumbnail,
            category_id=category_id
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('admin.posts'))

    # Fetch categories to display in the form
    categories = Category.query.all()
    return render_template('admin/add-post.html', categories=categories)

@admin_bp.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.name = request.form['name']
        post.description = request.form['description']
        # post.excerpt = request.form['excerpt']
        # post.thumbnail = request.form['thumbnail']
        post.category_id = request.form['category_id']
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('admin.posts'))
    categories = Category.query.all()
    return render_template('admin/edit-post.html', post=post, categories=categories)

@admin_bp.route('/post/delete/<int:id>', methods=['POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return jsonify({'success': True})  # Trả về JSON response để JavaScript biết yêu cầu thành công
    # return redirect(url_for('admin.posts'))

@admin_bp.route('/category/add-new', methods=['GET', 'POST'])
def add_new_category():
    if request.method == 'POST':
        name = request.form['name']
        # thumbnail = request.form['thumbnail']

        new_post = Category(
            name=name,
            # thumbnail=thumbnail,
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('admin.posts'))

    return render_template('admin/add-category.html')

@admin_bp.route('/category/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        # category.thumbnail = request.form['thumbnail']
        db.session.commit()
        flash('Category updated successfully!', 'success')
        return redirect(url_for('admin.posts'))
    return render_template('admin/edit-category.html', category=category)

@admin_bp.route('/category/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'success')
    return jsonify({'success': True})  # Trả về JSON response để JavaScript biết yêu cầu thành công
    # return redirect(url_for('admin.posts'))