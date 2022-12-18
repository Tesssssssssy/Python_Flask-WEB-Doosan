from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    auth = db.Column(db.String(50))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    gender = db.Column(db.String(100))
    graduation = db.Column(db.String(100))
    hearing = db.Column(db.String(100))
    sight = db.Column(db.String(100))
    
class Post(db.Model):                                        
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)             
    title = db.Column(db.String, nullable=False)             
    content = db.Column(db.String, nullable=False)    
    
class Comment(db.Model):
    __tablename__ = "comments" #테이블 이름 설정
    id = db.Column(db.Integer, primary_key=True)
    content =  db.Column(db.String, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    