# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from database import Base
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    password = Column(String(200), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, row_password):
        self.password = generate_password_hash(row_password)

    def check_password(self, row_password):
        result = check_password_hash(self.password, row_password)
        return result
