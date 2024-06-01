import os

from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from . import main
from app.crawler.crawl_data import fetch_data, parse_data, crawl_category

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/crawl', methods=['GET'])
def crawl():
    category_url = request.args.get('url', 'https://tuoitre.vn/cong-nghe')
    category_name = request.args.get('name', 'cong-nghe')
    crawl_category(category_url, category_name)
    return "Crawling and saving to database completed!"