import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from . import main
from app.crawler.crawl_data import fetch_data, parse_data, crawl_category
from ..models import Post, Category


@main.route('/')
def index():
    categories = Category.query.all()
    posts = Post.query.order_by(Post.created_date.desc()).limit(10).all()
    return render_template('main/index.html', categories=categories, posts=posts)
@main.route('/about')
def about():
    return render_template('main/about.html')
@main.route('/contact')
def contact():
    return render_template('main/contact.html')
@main.route('/posts', methods=['GET'])
def post():
    page = request.args.get('page', 1, type=int)
    all_posts = Post.query.order_by(Post.created_date.desc()).paginate(page=page, per_page=10)
    return render_template('main/posts.html', posts=all_posts)
@main.route('/post/<int:id>', methods=['GET'])
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('main/post_detail.html', post=post)
@main.route('/category/<int:category_id>', methods=['GET'])
def posts_by_category(category_id):
    page = request.args.get('page', 1, type=int)
    category = Category.query.get_or_404(category_id)
    posts = Post.query.order_by(Post.created_date.desc()).filter_by(category_id=category.id).paginate(page=page, per_page=10)
    return render_template('main/posts_by_category.html', category=category, posts=posts)


@main.route('/crawl', methods=['GET'])
def crawl():
    category_url = request.args.get('url', 'https://tuoitre.vn/cong-nghe')
    category_name = request.args.get('name', 'cong-nghe')
    crawl_category(category_url, category_name)
    return "Crawling and saving to database completed!"