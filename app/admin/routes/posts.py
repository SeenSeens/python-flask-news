from flask import render_template, request, redirect, url_for, flash, jsonify
from app.admin import admin_bp
from app.models.posts import Post
from app.models.categories import Category
from app import db
from utils.images import handle_image_upload, delete_image
from flask_login import login_required
from utils.decorators import admin_required


@admin_bp.route('/posts')
@login_required
@admin_required
def posts():
    # Lấy tất cả các chuyên mục từ database
    all_cat = Category.query.all()
    # Lấy tất cả các bài viết từ database
    all_posts = Post.query.all()
    return render_template('admin/pages/posts/posts.html', categories = all_cat, posts=all_posts)

@admin_bp.route('/post/add-new', methods=['GET', 'POST'])
@login_required
@admin_required
def add_new_posts():
    if request.method.__eq__('POST'):
        name = request.form['name']
        description = request.form['description']
        excerpt = request.form['excerpt']
        category_id = request.form['category_id']
        is_draft = request.form.get('is_draft', False)
        # Xử lý file upload
        file = request.files['thumbnail']
        filename = handle_image_upload(file)

        new_post = Post(
            name=name,
            description=description,
            excerpt=excerpt,
            thumbnail=filename,
            category_id=category_id,
            active=not is_draft
        )
        db.session.add(new_post)
        db.session.commit()
        if is_draft:
            flash('Bài viết đã được lưu thành bản nháp.', 'success')
        else:
            flash('Bài viết đã được tạo thành công.', 'success')
        return redirect(url_for('admin.posts'))

    # Fetch categories to display in the form
    categories = Category.query.all()
    return render_template('admin/pages/posts/add-post.html', categories=categories)

@admin_bp.route('/post/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    if request.method.__eq__('POST'):
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
@login_required
@admin_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return jsonify({'success': True})  # Trả về JSON response để JavaScript biết yêu cầu thành công
    # return redirect(url_for('admin.posts'))