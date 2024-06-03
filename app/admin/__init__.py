from flask import Blueprint
from flask_admin import Admin

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

admin = Admin(name='Admin Panel', template_mode='bootstrap3')

from . import routes, views