from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('admin.login'))
        elif not current_user.user_role:
            flash('You do not have the necessary permissions to access this page.', 'danger')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function
