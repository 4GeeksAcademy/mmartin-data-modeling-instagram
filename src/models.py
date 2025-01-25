import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(15), primary_key=True)
    email = Column(String(25), nullable=False)
    password = Column(String(30), nullable=False)
    posts = relationship("Post", back_populates="author")
    likes = relationship("Like", back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(15), ForeignKey('user.id'))
    content = Column(String(240), nullable=True)
    author = relationship("User")
    likes = relationship("Like")
    media = relationship("Media")
    comment = relationship("Comment")
class Likes(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(15), ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship("User")
    post = relationship("Post")
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    user_id = Column(String(15), ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String, nullable=False)
    user = relationship("User")
    post = relationship("Post")
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(String(15), ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    content = Column(String, nullable=True)
    user = relationship("User")
    post = relationship("Post")
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    follow_id = Column(String(15), ForeignKey('user.id'))
    user_id = Column(String(15), ForeignKey('user.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
