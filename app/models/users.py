from sqlalchemy import Column, String, Boolean
from app.models.base import BaseModel
from flask_login import LoginManager, UserMixin
login_manager = LoginManager()
login_manager.login_view = 'login'

# User model
class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __str__(self):
        return self.username


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))