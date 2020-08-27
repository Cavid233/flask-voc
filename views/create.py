from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging
from passlib.hash import sha256_crypt

create_b = Blueprint('create', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db



@create_b.route('/create',methods=['POST','GET'])
@login_required
def create():

    def getDict(file_name):
	    with open(file_name, encoding='utf-8') as file:
		    text = file.read()
	    text = text.replace('-', ' ')
	    return dict([l.split('\t') for l in text.splitlines() if l])

    if request.method == 'POST' and session['username'] == 'everyone':
        kind =  request.form.get('kind')
        title = request.form.get('title')
        answer = request.form.get('answer')
        author = session['username']


        #for a,b in getDict(r'C:\Users\Cavid\Desktop\deneme\new.txt').items():

        if kind == 'A1':
            newSual = Create(kind = kind,title = title.strip(),answer = answer.strip(), author = author)
        elif kind == 'A2':
            newSual = A2(kind = kind,title = title.strip(),answer = answer.strip(), author = author)
        elif kind == 'B1':
            newSual = B1(kind = kind,title = title.strip(),answer = answer.strip(), author = author)
        elif kind == 'B2':
            newSual = B2(kind = kind,title = title.strip(),answer = answer.strip(), author = author)
        else:
            newSual = Ielts_words(kind = kind,title = title.strip(),answer = answer.strip(), author = author)

        db.session.add(newSual)
        db.session.commit()

        return redirect(request.url)
    else:   
        return render_template('create.html')           









