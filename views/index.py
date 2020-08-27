from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

index_b = Blueprint('index', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db




@index_b.route('/',methods=['POST','GET'])
def index():
    if 'logged_in' in session:
        if session['kind'] == 'A1':
            return redirect(url_for('levels.test',id= session['A1_id']))
        elif session['kind'] == 'A2':
        
            return redirect(url_for('levels.test_A2',id= session['A2_id']))
        elif session['kind'] == 'B1':
            return redirect(url_for('levels.test_B1',id= session['B1_id']))
        elif session['kind'] == 'B2':
            return redirect(url_for('levels.test_B2',id= session['B2_id'] ))
        else:
            return redirect(url_for('levels.test_IE',id= session['IE_id'] ))
    else:
         return redirect(url_for('log_reg.login'))       