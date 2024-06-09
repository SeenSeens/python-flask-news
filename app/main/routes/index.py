from flask import render_template, request, redirect, url_for, send_from_directory, flash
from app.main import main
from app.crawler.crawl_data import  crawl_category
from app import app
from app.email import send_email
from app.models import Post, Category
@main.route('/')
def index():
    categories = Category.query.all()
    published_posts = (Post.query.filter_by(active=True)
                       .order_by(Post.created_date.desc())
                       .limit(10).all())
    return render_template('main/index.html', categories=categories, posts=published_posts)