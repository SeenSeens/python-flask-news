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
@main.route('/')
def index():
    categories = Category.query.all()
    published_posts = (Post.query.filter_by(active=True)
                       .order_by(Post.created_date.desc())
                       .limit(10).all())
    return render_template('main/index.html', categories=categories, posts=published_posts)
@main.route('/about')
def about():
    return render_template('main/about.html')
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email('New Contact Form Submission', 'truongtuan829@gmail.com', f'From: {name}\n\n{email}\n\n{phone}\n\n{message}')
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('main/contact.html')
@main.route('/posts', methods=['GET'])
def post():
    page = request.args.get('page', 1, type=int)
    all_posts = (Post
                 .query
                 .filter_by(active=True)
                 .order_by(Post.created_date
                 .desc()).paginate(page=page, per_page=10))
    return render_template('main/posts.html', posts=all_posts)
@main.route('/post/<int:id>', methods=['GET'])
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('main/post_detail.html', post=post)
@main.route('/category/<int:category_id>', methods=['GET'])
def posts_by_category(category_id):
    page = request.args.get('page', 1, type=int)
    category = Category.query.get_or_404(category_id)
    posts = (Post
             .query
             .filter_by(active=True)
             .order_by(Post.created_date.desc())
             .filter_by(category_id=category.id)
             .paginate(page=page, per_page=10))
    return render_template('main/posts_by_category.html', category=category, posts=posts)

@main.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)

@main.route('/crawl', methods=['GET'])
def crawl():
    category_url = request.args.get('url', 'https://tuoitre.vn/cong-nghe')
    category_name = request.args.get('name', 'cong-nghe')
    crawl_category(category_url, category_name)
    return "Crawling and saving to database completed!"