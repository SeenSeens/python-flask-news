from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Category(BaseModel):
    __tablename__ = 'role'

    name = Column(String(20), nullable=False)

    def __str__(self):
        return self.name