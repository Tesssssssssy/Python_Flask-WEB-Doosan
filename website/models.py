from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

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
    notes = db.relationship('Note')
    
# define Note Model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(2000))
    datetime = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    