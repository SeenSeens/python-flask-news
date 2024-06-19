from sqlalchemy import Column, Integer, String
from app import db
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    thumbnail = Column(String(100))