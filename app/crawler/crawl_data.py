import requests
from bs4 import BeautifulSoup
from app.models.categories import Category
from app.models.posts import Post
from app import app, db

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data from {url}")
        return None

def parse_data(html, category_name):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h3')  # Chỉnh sửa theo cấu trúc HTML của trang web

    with app.app_context():
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()

        for title in titles:
            post_title = title.get_text()
            post_url = title.find('a')['href'] if title.find('a') else None  # Chỉnh sửa theo cấu trúc HTML của trang web
            post_content = ''  # Bạn có thể cập nhật nội dung nếu cần thiết
            post = Post(name=post_title, url=post_url, description=post_content, category=category)
            db.session.add(post)

        db.session.commit()

def crawl_category(category_url, category_name):
    html = fetch_data(category_url)
    if html:
        parse_data(html, category_name)

if __name__ == "__main__":
    category_url = 'https://tuoitre.vn/cong-nghe'
    category_name = 'cong-nghe'
    crawl_category(category_url, category_name)
