from app import app
from flask_admin import Admin

admin = Admin(app=app, name='News Tech Administration', template_mode='bootstrap3')