import logging
from flask import Flask
from config import Config
from logging.handlers import TimedRotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Khởi tạo ứng dụng Flask
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config.from_object(Config)

# Khởi tạo SQLAlchemy và Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuration for media files
app.config['MEDIA_FOLDER'] = 'media'

# Configures the logging
def configure_logging(app):
    # Create a file handler which logs even debug messages
    handler = TimedRotatingFileHandler('flask-template.log', when='midnight', interval=1, backupCount=10)
    handler.setLevel(logging.INFO)  # Set the log level you want here
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

configure_logging(app)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app.admin import admin_bp, admin
app.register_blueprint(admin_bp, url_prefix='/admin')
# Initialize Flask-Admin
admin.init_app(app)

#from app.models import base, categories, posts  # Import models để chúng có thể được phát hiện bởi Flask-Migrate

