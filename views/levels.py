from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging
import random

from sqlalchemy import or_

levels_b = Blueprint('levels', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db,Register,Corrects


# Test sayfasi

# users_log = Register.query.filter_by(author = session['username']).first()

# number=users_log.A1


@levels_b.route('/test/', methods=['POST', 'GET'], defaults={'id' :1})
@levels_b.route('/test/<int:id>',methods=['POST','GET'])
@login_required
def test(id):
    #############################################################################
    infos = Punctuation_1.query.filter_by(author = session['username']).all()
    session['quantity']=len(infos)
    onfos = Punctuation_2.query.filter_by(author = session['username']).all()
    session['amounts']=len(onfos)

    cors = Corrects.query.filter_by(author = session['username']).all()
    session['cors_w']=len(cors)


    ##############################################################################

    l_test = Create.query.filter_by(id = id).filter(or_(Create.author == 'everyone', Create.author == session['username'])).first()

    #l_test = filter(or_(Create.author == 'leela', Create.author == 'akshay'))

    everyone= Create.query.filter_by(author = 'everyone').all()

    users_created = Create.query.filter_by(author = session['username']).all()

    others = everyone+users_created

    counts = len(others) 

    session['kind'] = 'A1'

    session['A1_id'] = id


    if id < counts+1 and l_test:       

        liste = []
        for oth in others:
            if oth.answer not in l_test.answer:
                liste.append(oth.answer)

        liste2 = random.sample(liste, 4)         
        liste2.append(l_test.answer) 
        results = random.sample(liste2, 5)
  
        return render_template('run.html', id = id,l_test = l_test, results =results,counts =counts,others=others)         
    else:
        return render_template('run.html')



# Test sayfasi
@levels_b.route('/test_A2/', methods=['POST', 'GET'], defaults={'id' : 1})
@levels_b.route('/test_A2/<int:id>',methods=['POST','GET'])
@login_required
def test_A2(id):
    #############################################################################
    infos = Punctuation_1.query.filter_by(author = session['username']).all()
    session['quantity']=len(infos)
    onfos = Punctuation_2.query.filter_by(author = session['username']).all()
    session['amounts']=len(onfos)

    cors = Corrects.query.filter_by(author = session['username']).all()
    session['cors_w']=len(cors)
    ##############################################################################

    l_test = A2.query.filter_by(id = id).filter(or_(Create.author == 'everyone', Create.author == session['username'])).first()

    #l_test = filter(or_(Create.author == 'leela', Create.author == 'akshay'))

    everyone= A2.query.filter_by(author = 'everyone').all()

    users_created = A2.query.filter_by(author = session['username']).all()

    others = everyone+users_created

    counts = len(others) 

    session['kind'] = 'A2'
    session['A2_id'] = id


    if id < counts+1 and l_test:       

        liste = []
        for oth in others:
            if oth.answer not in l_test.answer:
                liste.append(oth.answer)

        liste2 = random.sample(liste, 4)         
        liste2.append(l_test.answer) 
        results = random.sample(liste2, 5)
  
        return render_template('run.html', id = id,l_test = l_test, results =results,counts =counts,others=others)         
    else:
        return render_template('run.html')


# Test sayfasi
@levels_b.route('/test_B1/', methods=['POST', 'GET'], defaults={'id' : 1})
@levels_b.route('/test_B1/<int:id>',methods=['POST','GET'])
@login_required
def test_B1(id):
    #############################################################################
    infos = Punctuation_1.query.filter_by(author = session['username']).all()
    session['quantity']=len(infos)
    onfos = Punctuation_2.query.filter_by(author = session['username']).all()
    session['amounts']=len(onfos)

    cors = Corrects.query.filter_by(author = session['username']).all()
    session['cors_w']=len(cors)
    ##############################################################################

    l_test = B1.query.filter_by(id = id).filter(or_(Create.author == 'everyone', Create.author == session['username'])).first()

    #l_test = filter(or_(Create.author == 'leela', Create.author == 'akshay'))

    everyone= B1.query.filter_by(author = 'everyone').all()

    users_created = B1.query.filter_by(author = session['username']).all()

    others = everyone+users_created

    counts = len(others) 

    session['kind'] = 'B1'

    session['B1_id'] = id


    if id < counts+1 and l_test:       

        liste = []
        for oth in others:
            if oth.answer not in l_test.answer:
                liste.append(oth.answer)

        liste2 = random.sample(liste, 4)         
        liste2.append(l_test.answer) 
        results = random.sample(liste2, 5)
  
        return render_template('run.html', id = id,l_test = l_test, results =results,counts =counts,others=others)         
    else:
        return render_template('run.html')


# Test sayfasi
@levels_b.route('/test_B2/', methods=['POST', 'GET'], defaults={'id' : 1})
@levels_b.route('/test_B2/<int:id>',methods=['POST','GET'])
@login_required
def test_B2(id):
    #############################################################################
    infos = Punctuation_1.query.filter_by(author = session['username']).all()
    session['quantity']=len(infos)
    onfos = Punctuation_2.query.filter_by(author = session['username']).all()
    session['amounts']=len(onfos)

    cors = Corrects.query.filter_by(author = session['username']).all()
    session['cors_w']=len(cors)
    ##############################################################################

    l_test = B2.query.filter_by(id = id).filter(or_(Create.author == 'everyone', Create.author == session['username'])).first()

    #l_test = filter(or_(Create.author == 'leela', Create.author == 'akshay'))

    everyone= B2.query.filter_by(author = 'everyone').all()

    users_created = B2.query.filter_by(author = session['username']).all()

    others = everyone+users_created

    counts = len(others) 

    session['kind'] = 'B2'

    session['B2_id'] = 1
    session['B2_id'] = id


    if id < counts+1 and l_test:       

        liste = []
        for oth in others:
            if oth.answer not in l_test.answer:
                liste.append(oth.answer)

        liste2 = random.sample(liste, 4)         
        liste2.append(l_test.answer) 
        results = random.sample(liste2, 5)
  
        return render_template('run.html', id = id,l_test = l_test, results =results,counts =counts,others=others)         
    else:
        return render_template('run.html')      



# Test sayfasi
@levels_b.route('/test_IE/', methods=['POST', 'GET'], defaults={'id' : 1})
@levels_b.route('/test_IE/<int:id>',methods=['POST','GET'])
@login_required
def test_IE(id):
    #############################################################################
    infos = Punctuation_1.query.filter_by(author = session['username']).all()
    session['quantity']=len(infos)
    onfos = Punctuation_2.query.filter_by(author = session['username']).all()
    session['amounts']=len(onfos)

    cors = Corrects.query.filter_by(author = session['username']).all()
    session['cors_w']=len(cors)
    ##############################################################################

    l_test = Ielts_words.query.filter_by(id = id).filter(or_(Create.author == 'everyone', Create.author == session['username'])).first()

    #l_test = filter(or_(Create.author == 'leela', Create.author == 'akshay'))

    everyone= Ielts_words.query.filter_by(author = 'everyone').all()

    users_created = Ielts_words.query.filter_by(author = session['username']).all()

    others = everyone+users_created

    counts = len(others) 

    session['kind'] = 'IE'

    session['id'] = 1
    session['IE_id'] = id


    if id < counts+1 and l_test:       

        liste = []
        for oth in others:
            if oth.answer not in l_test.answer:
                liste.append(oth.answer)

        liste2 = random.sample(liste, 4)         
        liste2.append(l_test.answer) 
        results = random.sample(liste2, 5)
  
        return render_template('run.html', id = id,l_test = l_test, results =results,counts =counts,others=others)         
    else:
        return render_template('run.html')  