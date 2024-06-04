from flask import Blueprint
from flask_admin import Admin
from flask_login import LoginManager

from .. import app
from ..models import User

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

admin = Admin(name='Admin Panel', template_mode='bootstrap3')

login_manager = LoginManager(app)
login_manager.login_view = 'admin.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from . import routes, views, middleware
