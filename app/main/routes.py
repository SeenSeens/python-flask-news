from flask import render_template, request, redirect, url_for, send_from_directory, flash
from . import main
from app.crawler.crawl_data import  crawl_category
from app import app
from ..email import send_email
from ..models import Post, Category

# Context processor to make categories available in all templates
@main.context_processor
def inject_categories():
    categories = Category.query.all()
    return dict(categories=categories)







@main.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)

@main.route('/crawl', methods=['GET'])
def crawl():
    category_url = request.args.get('url', 'https://tuoitre.vn/cong-nghe')
    category_name = request.args.get('name', 'cong-nghe')
    crawl_category(category_url, category_name)
    return "Crawling and saving to database completed!"