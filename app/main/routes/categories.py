from flask import render_template, request
from app.main import main
from app.models import Post, Category
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