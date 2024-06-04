from flask import render_template, request, redirect, url_for, flash, jsonify
from app.admin import admin_bp
from app.models.categories import Category
from app import db
from utils.images import handle_image_upload, delete_image
from flask_login import login_required
from utils.decorators import admin_required
@admin_bp.route('/category/add-new', methods=['GET', 'POST'])
@login_required
@admin_required
def add_new_category():
    if request.method.__eq__('POST'):
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
@login_required
@admin_required
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method.__eq__('POST'):
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
@login_required
@admin_required
def delete_category(id):
    category = Category.query.get_or_404(id)
    # Xóa hình ảnh
    delete_image(category.thumbnail)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'success')
    return jsonify({'success': True})  # Trả về JSON response để JavaScript biết yêu cầu thành công
    # return redirect(url_for('admin.posts'))