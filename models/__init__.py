from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector
from tkinter import messagebox

from sqlalchemy.orm import relationship

SQLAlchemyBase = declarative_base()


class CustomBaseModel:
    id = Column(INTEGER, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Book(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = "books"
    name = Column(VARCHAR(45), nullable=False)
    author = Column(VARCHAR(45), nullable=False)
    year = Column(Integer)
    ISBN = Column(VARCHAR(45), nullable=False, unique=True)
    borrowed = Column(Boolean, nullable=False)


class User(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = "users"
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)


class BookForUser(SQLAlchemyBase, CustomBaseModel):
    __tablename__ = "book_for_user"
    user_id = Column(INTEGER, ForeignKey('users.id'))
    user = relationship('Book')

