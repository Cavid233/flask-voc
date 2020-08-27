from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

dash_fil_b = Blueprint('dash_fil', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db


@dash_fil_b.route('/dashboard')
@login_required
def dashboard():

    everyone= Create.query.filter_by(author = 'everyone').all()
    #users_created = Create.query.filter_by(author = session['username']).all()
    q_A2 = A2.query.all()
    q_B1 = B1.query.filter_by(author = 'everyone').all()
    q_B2 = B2.query.filter_by(author = 'everyone').all()
    artus = everyone+q_A2+q_B1+q_B2

    if artus:
        return render_template('dashboard.html',artus = artus)
    else:
        return render_template('dashboard.html')



@dash_fil_b.route('/filter/<string:kind>',methods=['POST','GET'])
@login_required
def filter(kind):
    if kind == 'A1':
        artus = Create.query.all()
        return render_template('dashboard.html',artus = artus)

    elif kind == 'A2':
        artus = A2.query.all()
        return  render_template('dashboard.html',artus = artus)

    elif kind == 'B1':
        artus = B1.query.all()
        return  render_template('dashboard.html',artus = artus)

    elif kind == 'B2':
        artus = B2.query.all()
        return  render_template('dashboard.html',artus = artus )
            
    else:    
        artus = Ielts_words.query.all()
        return  render_template('dashboard.html',artus = artus)
