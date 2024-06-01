from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from app import db
from app.models.categories import Category
from app.models.posts import Post

from . import admin, admin_bp

class AdminModelView(ModelView):
    def is_accessible(self):
        # Customize this method to control access
        return True

    def inaccessible_callback(self, name, **kwargs):
        # Redirect to login page or show error
        return redirect(url_for('login'))

# Add views to admin
admin.add_view(AdminModelView(Category, db.session))
admin.add_view(AdminModelView(Post, db.session))
