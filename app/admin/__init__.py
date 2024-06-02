from flask import Blueprint
from flask_admin import Admin
from app import app, db
from flask_admin.contrib.sqla import ModelView
from app.models.categories import Category
from app.models.posts import Post

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

admin = Admin(name='Admin Panel', template_mode='bootstrap3')

from . import routes, views