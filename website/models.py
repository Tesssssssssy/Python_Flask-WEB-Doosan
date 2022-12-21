from . import db 
from flask_login import UserMixin
import datetime

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

class Info(db.Model):
    __tablename__ = 'infos'
    id = db.Column(db.Integer, primary_key=True)
    drink = db.Column(db.String(300))
    sleephour = db.Column(db.String(300))
    sleepqual = db.Column(db.String(300))
    tired = db.Column(db.String(300))
    anxiety = db.Column(db.String(300))
    gloom = db.Column(db.String(300))
    createdat = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, drink, sleephour, sleepqual, tired, anxiety, gloom):
        self.drink = drink
        self.sleephour = sleephour
        self.sleepqual = sleepqual
        self.tired = tired
        self.anxiety = anxiety
        self.gloom = gloom
        self.createdat = datetime.datetime.today()
        
class Post(db.Model):                                        
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)             
    title = db.Column(db.String, nullable=False)             
    content = db.Column(db.String, nullable=False) 
    created_at = db.Column(db.DateTime)
    comments = db.relationship('Comment',backref='post')  
    
        # 생성자
    def __init__(self,title,content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.today() 
        
    
class Comment(db.Model):
    __tablename__ ='comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))  
    created_at = db.Column(db.DateTime)
    creator = db.Column(db.String)
    
    def __init__(self,content,creator):
        self.content = content
        self.created_at = datetime.datetime.today()
        self.creator = creator
        
    