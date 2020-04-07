# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from database import Base
from werkzeug.security import generate_password_hash, check_password_hash  # 密码保护，使用hash方法


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    password = Column(String(200), nullable=False)  # 内部使用

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):  # 定义一个外部使用的密码
        return self.password

    @password.setter  # 设置密码加密
    def password(self, row_password):
        self.password = generate_password_hash(row_password)

    def check_password(self, row_password):  # 定义一个反向解密的函数
        result = check_password_hash(self.password, row_password)
        return result
