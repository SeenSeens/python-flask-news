from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db, create_app
from datetime import datetime
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    posts = relationship('Post', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Post(BaseModel):
    __tablename__ = 'post'

    name = Column(String(50), nullable=False)
    description = Column(Text())
    excerpt = Column(String(255))
    thumbnail = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


app = create_app()
with app.app_context():
    db.create_all()