from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Enum
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import BaseModel
from flask_login import UserMixin
from enum import Enum as UserEnum

# User model
class UserRole(UserEnum):
    ADMIN = 1
    USER = 2
class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    name = Column(String(50), nullable=False)
    username = Column(String(50),unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean(), default=True)
    join_date = Column(DateTime(), default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    def __str__(self):
        return self.username