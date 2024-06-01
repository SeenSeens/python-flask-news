from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    posts = relationship('Post', backref='category', lazy=True)

    def __str__(self):
        return self.name