from flask import render_template, request, redirect, url_for, send_from_directory, flash
from app.main import main
from app.crawler.crawl_data import  crawl_category
from app import app
from app.email import send_email
from app.models import Post, Category
@main.route('/about')
def about():
    return render_template('main/about.html')