import hashlib

from flask import render_template, request, flash, redirect, url_for, jsonify

from app import db
from app.admin import admin_bp
from flask_login import login_required

from app.models import User
from app.models.users import UserRole
from utils.auth import update_user
from utils.decorators import admin_required
from utils.images import delete_image, handle_image_upload


@admin_bp.route('/accounts')
@login_required
@admin_required
def accounts():
    users = User.query.all()
    return render_template('admin/pages/accounts/accounts.html', users=users)
@admin_bp.route('/user/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(id):
    user = User.query.get_or_404(id)
    err_msg = ''
    if request.method.__eq__('POST'):
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']
        user_role = request.form['user_role']
        avatar_path = None

        if password != confirm:
            err_msg = 'Mật khẩu không khớp'
        else:
            avatar_path = user.thumbnail
            if 'thumbnail' in request.files:
                image = request.files['thumbnail']
                if image.filename != '':
                    if user.thumbnail:
                        delete_image(user.thumbnail)
                    avatar_path = handle_image_upload(image)

            update_user(user_id=user.id, name=name, username=username, email=email, password=password,
                        thumbnail=avatar_path, user_role=user_role)
            flash('Cập nhật người dùng thành công!', 'success')
            return redirect(url_for('admin.accounts'))

    return render_template('admin/pages/accounts/edit-account.html', user=user, err_msg=err_msg, UserRole=UserRole)

@admin_bp.route('/user/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    # Xóa hình ảnh
    delete_image(user.thumbnail)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return jsonify({'success': True})  # Trả về JSON response để JavaScript biết yêu cầu thành công