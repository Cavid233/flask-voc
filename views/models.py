from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)

db = SQLAlchemy(app)

#Kullanici Giris Decoratoru
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login to enter this page','danger')
            return redirect(url_for('login'))    
    return decorated_function

class Create(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(10), nullable=False)

class A2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(10), nullable=False)    


class B1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(10), nullable=False)    


class B2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(10), nullable=False)      


class Ielts_words(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(10), nullable=False)      

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    username = db.Column(db.String(10))
    email = db.Column(db.String(10))
    password = db.Column(db.String(10))
    A1 = db.Column(db.Integer, default=1)
    A2 = db.Column(db.Integer, default=1)
    B1 = db.Column(db.Integer, default=1)
    B2 = db.Column(db.Integer, default=1)
    IE = db.Column(db.Integer, default=1)

class Punctuation_1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False)
    author = db.Column(db.String(10), nullable=False)

class Punctuation_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False) 
    author = db.Column(db.String(10), nullable=False)

class Corrects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    answer = db.Column(db.String(10), nullable=False) 
    author = db.Column(db.String(10), nullable=False)
