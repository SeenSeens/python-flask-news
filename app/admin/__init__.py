from flask import Blueprint
from flask_admin import Admin
from app import app, db
from app.admin.views import CustomCategoryView, CustomPostView
from app.models.categories import Category
from app.models.posts import Post

admin_bp = Blueprint('admin', __name__)

admin = Admin(name='Admin Panel', template_mode='bootstrap3')
admin.add_view(CustomCategoryView(Category, db.session))
admin.add_view(CustomPostView(Post, db.session))

from . import routes, views