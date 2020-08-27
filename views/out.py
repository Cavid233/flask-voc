from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

out_b = Blueprint('out', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db

        
@out_b.route("/out_exclamation/",methods = ['GET','POST'])
@login_required
def out_exclamation():

    infos = Punctuation_1.query.filter_by(author = session['username']).all()
    session['quantity']=len(infos)

    if infos:
       
        return render_template('exclamation.html',infos=infos)
    else:
        return render_template('exclamation.html')



@out_b.route("/out_question_circle/",methods = ['GET','POST'])
@login_required
def out_question_circle():

    onfos = Punctuation_2.query.filter_by(author = session['username']).all()
    session['amounts']=len(onfos)

    if onfos:
       
        return render_template('question_circle.html',onfos = onfos)
    else:
        return render_template('question_circle.html')        