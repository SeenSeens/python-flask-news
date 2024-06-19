from flask import Blueprint
main = Blueprint('main', __name__)

from . import routes
from .routes import index, posts, about, categories, contact, auth
