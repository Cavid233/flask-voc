from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

punc_b = Blueprint('punc', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db

@punc_b.route("/punctuation_1/<int:id>",methods = ['GET','POST'])
@login_required
def punctuation_1(id):
    if session['kind'] == 'A1':
        punctuation_1 = Create.query.filter_by(id = id).first()
        skip = 'levels.test'
    elif session['kind'] == 'A2':
        punctuation_1 = A2.query.filter_by(id = id).first()
        skip = 'levels.test_A2'
    elif session['kind'] == 'B1':
        punctuation_1 = B1.query.filter_by(id = id).first()
        skip = 'levels.test_B1'
    elif session['kind'] == 'B2':
        punctuation_1 = B2.query.filter_by(id = id).first()
        skip = 'levels.test_B2'
    else:
        punctuation_1 = Ielts_words.query.filter_by(id = id).first()
        skip = 'levels.test_IE'

    if punctuation_1:

        newPunctuation_1 = Punctuation_1(kind = punctuation_1.kind, title = punctuation_1.title,
                                        answer = punctuation_1.answer,author=session['username'])
        db.session.add(newPunctuation_1)
        db.session.commit()

        return redirect(url_for(skip,id=id+1))
    else:
        return redirect(url_for('create'))  


@punc_b.route("/punctuation_2/<int:id>",methods = ['GET','POST'])
@login_required
def punctuation_2(id):

    if session['kind'] == 'A1':
        punctuation_2 = Create.query.filter_by(id = id).first()
        skip = 'levels.test'

    elif session['kind'] == 'A2':
        punctuation_2 = A2.query.filter_by(id = id).first()
        skip = 'levels.test_A2'
    elif session['kind'] == 'B1':
        punctuation_2 = B1.query.filter_by(id = id).first()
        skip = 'levels.test_B1'
    elif session['kind'] == 'B2':
        punctuation_2 = B2.query.filter_by(id = id).first()
        skip = 'levels.test_B2'
    else:
        punctuation_2 = Ielts_words.query.filter_by(id = id).first()
        skip = 'levels.test_IE'


    if punctuation_2:

        newPunctuation_2 = Punctuation_2(kind = punctuation_2.kind, title = punctuation_2.title,
                                         answer = punctuation_2.answer,author=session['username'])
        db.session.add(newPunctuation_2)
        db.session.commit()

        return redirect(url_for(skip,id=id+1))
    else:
        return redirect(url_for('create'))   

