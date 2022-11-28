from . import db 
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    gender = db.Column(db.String(100))
    graduation = db.Column(db.String(100))
    hearing = db.Column(db.String(100))
    sight = db.Column(db.String(100))
    