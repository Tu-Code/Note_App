from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER
from flask_login import UserMixin
from sqlalchemy.sql import func

class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, unique=True)
    activity = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    participants = db.Column(db.Integer)
    price = db.Column(db.Integer)
    link = db.Column(db.String(500), nullable=True)
    activities = db.relationship('UserActivity', lazy = True, backref = 'activity')
    
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    activities = db.relationship('UserActivity', lazy = True, backref = 'user')

class UserActivity(db.Model):
    __tablename__ = 'useractivity'
    id = db.Column( db.Integer, primary_key = True, autoincrement = True )
    uid = db.Column( db.Integer, db.ForeignKey('user.id'), nullable = False )
    aid = db.Column( INTEGER(unsigned=True), db.ForeignKey('activity.id'), nullable = False )