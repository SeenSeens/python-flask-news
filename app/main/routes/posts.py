from flask import render_template, request
from app.main import main
from app.models import Post, Category


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