from flask import render_template, request, redirect, url_for, send_from_directory, flash
from app.main import main
from app.crawler.crawl_data import  crawl_category
from app import app
from app.models import Category, Post


# Context processor to make categories available in all templates
@main.context_processor
def inject_categories():
    categories = Category.query.all()
    return dict(categories=categories)
@main.context_processor
def get_recent_posts():
    recent_posts = Post.query.filter_by(active=True).order_by(Post.created_date.desc()).limit(5).all()
    return dict(recent_posts=recent_posts)

# @main.context_processor
# def search():
#     query = request.args.get('query', '')
#     search_results = []
#     if query:
#         search_results = Post.query.filter(Post.title.contains(query) | Post.content.contains(query)).all()
#     return render_template('main/index.html', search_results=search_results, query=query)
# @main.context_processor
# def search_posts(query):
#     if query:
#         search_results = Post.query.filter(Post.title.contains(query) | Post.content.contains(query)).all()
#     else:
#         search_results = []
#     return search_results
# @main.context_processor
# def inject_search():
#     def search(query):
#         return search_posts(query)
#     return dict(search=search)

@main.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)

@main.route('/crawl', methods=['GET'])
def crawl():
    category_url = request.args.get('url', 'https://tuoitre.vn/cong-nghe')
    category_name = request.args.get('name', 'cong-nghe')
    crawl_category(category_url, category_name)
    return "Crawling and saving to database completed!"