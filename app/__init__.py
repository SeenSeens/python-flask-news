import os
import logging
from flask import Flask, send_from_directory
from flask_mail import Mail
from config import Config
from logging.handlers import TimedRotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import cloudinary

cloudinary.config(
    cloud_name="dqogaxemt",
    api_key="185533732234982",
    api_secret="boacO5AeE5GSaClvKVmg1YTIjJY",
    secure=True,
)


# Khởi tạo ứng dụng Flask
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config.from_object(Config)

# Tạo thư mục lưu trữ media nếu chưa tồn tại
# if not os.path.exists(app.config['MEDIA_FOLDER']):
#     os.makedirs(app.config['MEDIA_FOLDER'])

# Khởi tạo SQLAlchemy và Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

# Configuration for media files
app.config['MEDIA_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'media')
app.config['MEDIA_URL'] = '/media/'

# Configures the logging
def configure_logging(app):
    # Create a file handler which logs even debug messages
    handler = TimedRotatingFileHandler('flask-template.log', when='midnight', interval=1, backupCount=10)
    handler.setLevel(logging.INFO)  # Set the log level you want here
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

configure_logging(app)

from app.main import main
app.register_blueprint(main)

from app.admin import admin_bp, admin

app.register_blueprint(admin_bp)

#from app.models import base, categories, posts  # Import models để chúng có thể được phát hiện bởi Flask-Migrate

# Serve media files
@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)