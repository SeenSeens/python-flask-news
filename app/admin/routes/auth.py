from flask import render_template, request, redirect, url_for
from utils import auth
from app.admin import admin_bp
import cloudinary.uploader
from flask_login import login_user, logout_user, login_required
from utils.decorators import admin_required
@admin_bp.route('/register', methods=['GET', 'POST'])
def register():
    err_msg = ''
    if request.method.__eq__('POST'):
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']
        avatar_path = None
        try:
            if password.strip().__eq__(confirm.strip()):
                thumbnail = request.files['thumbnail']
                if thumbnail:
                    res = cloudinary.uploader.upload(thumbnail)
                    avatar_path = res['secure_url']
                auth.add_user(name=name, username=username, email=email, password=password, thumbnail=avatar_path)
                return redirect(url_for('admin.dashboard'))
            else:
                err_msg = 'Mật khẩu không khớp'
        except Exception as ex:
            err_msg = 'Hệ thống đang có lỗi: ' + str(ex)

    return render_template('admin/pages/accounts/register.html', err_msg=err_msg)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form['username']
        password = request.form['password']

        user = auth.check_login(username=username, password=password)
        if user:
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            err_msg = 'Tài khoản hoặc mật khẩu không chính xác'
    return render_template('admin/pages/accounts/login.html', err_msg=err_msg)

@admin_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))