from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

correct_b = Blueprint('correct', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db,Corrects


@correct_b.route('/correct/<int:id>/<string:answer>',methods=['POST','GET'])
def correct(id,answer):
    session['correct']+=1
 
 

    if session['kind'] == 'A1':
        correct_1 = Create.query.filter_by(answer = answer).first()
        skip = 'levels.test'
    elif session['kind'] == 'A2':
        correct_1 = A2.query.filter_by(answer = answer).first()
        skip = 'levels.test_A2'
    elif session['kind'] == 'B1':
        correct_1 = B1.query.filter_by(answer = answer).first()
        skip = 'levels.test_B1'
    elif session['kind'] == 'B2':
        correct_1 = B2.query.filter_by(answer = answer).first()
        skip = 'levels.test_B2'
    else:
        correct_1 = Ielts_words.query.filter_by(answer = answer).first()
        skip = 'levels.test_IE'

    if correct_1:

        newCorrect_1 = Corrects(kind = correct_1.kind, title = correct_1.title,
                                        answer = correct_1.answer,author=session['username'])
        db.session.add(newCorrect_1)
        db.session.commit()

        return redirect(url_for(skip,id=id+1))
    else:
        return redirect(url_for('create'))      






@correct_b.route("/correct/",methods = ['GET','POST'])
@login_required
def correct_1():

    cors = Corrects.query.filter_by(author = session['username']).all()
    
    cors = Corrects.query.filter_by(author = session['username']).all()
    session['cors_w']=len(cors)
    
    if cors:
       
        return render_template('correct.html',cors = cors)
    else:
        return render_template('correct.html')                  