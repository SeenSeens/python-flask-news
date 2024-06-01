from sqlalchemy import Column, Integer
from app import db
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)