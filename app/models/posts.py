from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey, Integer
from app.models.base import BaseModel
from app.models.categories import Category
from datetime import datetime
class Post(BaseModel):
    __tablename__ = 'post'
    name = Column(String(50), nullable=False)
    description = Column(Text())
    excerpt = Column(String(255))
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name