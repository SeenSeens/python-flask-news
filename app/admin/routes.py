import os

from flask import render_template, request, redirect, url_for, flash, jsonify, send_from_directory, current_app
from werkzeug.utils import secure_filename
from . import admin_bp
from app.models.posts import Post
from app.models.categories import Category
from app import db, app
from utils.images import handle_image_upload, delete_image


@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/accounts')
def accounts():
    return render_template('admin/pages/accounts/accounts.html')

@admin_bp.route('/posts')
def posts():
    # Lấy tất cả các chuyên mục từ database
    all_cat = Category.query.all()
    # Lấy tất cả các bài viết từ database
    all_posts = Post.query.all()
    return render_template('admin/pages/posts/posts.html', categories = all_cat, posts=all_posts)

@admin_bp.route('/post/add-new', methods=['GET', 'POST'])
def add_new_posts():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        excerpt = request.form['excerpt']
        category_id = request.form['category_id']
        # Xử lý file upload
        file = request.files['thumbnail']
        filename = handle_image_upload(file)

        new_post = Post(
            name=name,
            description=description,
            excerpt=excerpt,
            thumbnail=filename,
            category_id=category_id
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('admin.posts'))

    # Fetch categories to display in the form
    categories = Category.query.all()
    return render_template('admin/pages/posts/add-post.html', categories=categories)

@admin_bp.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.name = request.form['name']
        post.description = request.form['description']
        post.excerpt = request.form['excerpt']
        post.category_id = request.form['category_id']
        # Xử lý file upload
        if 'thumbnail' in request.files:
            image = request.files['thumbnail']
            if image.filename != '':
                if post.thumbnail:
                    delete_image(post.thumbnail)
                filename = handle_image_upload(image)
                post.thumbnail = filename

        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('admin.posts'))
    categories = Category.query.all()
    return render_template('admin/pages/posts/edit-post.html', post=post, categories=categories)

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
        # Xử lý file upload
        file = request.files['thumbnail']
        filename = handle_image_upload(file)
        new_post = Category(
            name=name,
            thumbnail=filename  # Lưu tên file vào database
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('admin.posts'))
    return render_template('admin/pages/category/add-category.html')

@admin_bp.route('/category/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        # Xử lý file upload
        if 'thumbnail' in request.files:
            image = request.files['thumbnail']
            if image.filename != '':
                if category.thumbnail:
                    delete_image(category.thumbnail)
                filename = handle_image_upload(image)
                category.thumbnail = filename

        db.session.commit()
        flash('Category updated successfully!', 'success')
        return redirect(url_for('admin.posts'))
    return render_template('admin/pages/category/edit-category.html', category=category)

@admin_bp.route('/category/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    # Xóa hình ảnh
    delete_image(category.thumbnail)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'success')
    return jsonify({'success': True})  # Trả về JSON response để JavaScript biết yêu cầu thành công
    # return redirect(url_for('admin.posts'))


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

# Thêm route để phục vụ các tệp phương tiện
from flask import send_from_directory

@admin_bp.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config['MEDIA_FOLDER'], filename)