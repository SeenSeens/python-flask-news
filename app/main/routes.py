import os

from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from . import main

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')