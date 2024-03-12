import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, LargeBinary
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    bio = Column(Text)
    profile_picture = Column(LargeBinary)
    date_joined = Column(Date)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    caption = Column(Text)
    image = Column(LargeBinary)
    date_posted = Column(Date)
    user = relationship('User')

class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    follower_user_id = Column(Integer, ForeignKey('user.id'))
    followed_user_id = Column(Integer, ForeignKey('user.id'))
    date_followed = Column(Date)
    follower = relationship('User', foreign_keys=[follower_user_id])
    followed = relationship('User', foreign_keys=[followed_user_id])

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    date_liked = Column(Date)
    user = relationship('User')
    post = relationship('Post')

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e