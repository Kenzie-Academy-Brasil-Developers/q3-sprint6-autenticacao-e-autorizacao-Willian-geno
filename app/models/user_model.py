from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import VARCHAR, Column, Integer, String



@dataclass
class UserModel(db.Model):
    name: str
    last_name:str
    email:str
    api_key:str

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(124), nullable=False)
    last_name = Column(VARCHAR(511), nullable = False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password_hash= Column(VARCHAR(511), nullable=False)
    api_key = Column(VARCHAR(511), nullable=False)

""" user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(64), unique=True, nullable=False)"""