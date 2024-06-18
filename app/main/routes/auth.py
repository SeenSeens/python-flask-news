from flask import render_template, request, redirect, url_for, jsonify
from utils import auth
from app.main import main
import cloudinary.uploader
from flask_login import login_user, logout_user
@main.route('/register', methods=['GET', 'POST'])
def register():
    response = {'status': 'success'}

    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        avatar_path = None

        # Kiểm tra nếu có bất kỳ trường nào bị thiếu
        if not all([name, username, email, password, confirm]):
            response['status'] = 'error'
            response['message'] = 'Vui lòng điền đầy đủ thông tin'
            return jsonify(response)

        # Kiểm tra mật khẩu khớp nhau
        if password.strip() != confirm.strip():
            response['status'] = 'error'
            response['message'] = 'Mật khẩu không khớp'
            return jsonify(response)

        try:
            thumbnail = request.files.get('thumbnail')
            if thumbnail:
                res = cloudinary.uploader.upload(thumbnail)
                avatar_path = res['secure_url']

            # Thêm người dùng vào hệ thống
            auth.add_user(name=name, username=username, email=email, password=password, thumbnail=avatar_path)

            response['message'] = 'Đăng ký thành công'
            return jsonify(response)

        except Exception as ex:
            response['status'] = 'error'
            response['message'] = 'Hệ thống đang có lỗi: ' + str(ex)
            return jsonify(response)

    # Nếu không phải POST request, trả về lỗi
    response['status'] = 'error'
    response['message'] = 'Invalid request method'
    return jsonify(response)
'''
def register():
    response = {'status': 'success'}
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
                return redirect(url_for('main.index'))
            else:
                response['status'] = 'error'
                response['message'] = 'Mật khẩu không khớp'
        except Exception as ex:
            response['status'] = 'error'
            response['message'] = 'Hệ thống đang có lỗi: ' + str(ex)

    return jsonify(response)
'''

@main.route('/login', methods=['GET', 'POST'])
def login():
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form['username']
        password = request.form['password']

        user = auth.check_login(username=username, password=password)
        if user:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            err_msg = 'Tài khoản hoặc mật khẩu không chính xác'
    return render_template('main/index.html', err_msg=err_msg)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))