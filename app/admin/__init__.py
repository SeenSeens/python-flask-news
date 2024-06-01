from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
admin_bp = Blueprint('admin', __name__)
admin = Admin(name='Admin Panel', template_mode='bootstrap3')

from . import routes
from . import views