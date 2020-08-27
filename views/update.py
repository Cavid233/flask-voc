from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

update_b = Blueprint('update', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db

# Test Guncelleme
@update_b.route('/update/<string:kind>/<string:id>',methods = ['GET','POST'])
@login_required
def update(id,kind):
    if session['username'] == 'everyone':
        if request.method == 'GET':
            if kind == 'A1':
                l_update = Create.query.filter_by(id = id).first()

            elif kind == 'A2':
                l_update = A2.query.filter_by(id = id).first()

            elif kind == 'B1':
                l_update = B1.query.filter_by(id = id).first()

            elif kind == 'B2':
                l_update = B2.query.filter_by(id = id).first()

            else:    
                l_update = Ielts_words.query.filter_by(id = id).first()

            if l_update and l_update.author == session['username']:

                u_kind= l_update.kind
                u_title = l_update.title
                u_answer = l_update.answer

                return render_template('update.html', u_kind = u_kind, u_title = u_title, u_answer = u_answer)

            else:
                flash('No such question or authority','danger')
                return redirect(url_for('dash_fil.dashboard'))
        else:
            #Post request 

            d_kind = request.form.get('d_kind')
            d_title = request.form.get('d_title')
            d_answer = request.form.get('d_answer')

            if d_kind == 'A1':
                user = Create.query.get(id)

            elif d_kind == 'A2':
                user = A2.query.get(id)

            elif d_kind == 'B1':
                user = B1.query.get(id)

            elif d_kind == 'B2':
                user = B2.query.get(id)

            else:    
                user = Ielts_words.query.get(id)
            #######################################################
            if user:
                user.title =  d_title
                user.answer =  d_answer
                db.session.commit()

                flash('Question Successfully Updated','success')

                return redirect(url_for('dash_fil.dashboard')) 
            else:
                flash("Choose correctly word's Kind",'danger')
                return redirect(url_for('dash_fil.dashboard'))    
    else:
        flash("Please don't try to do this again",'danger')
        return redirect(url_for('dash_fil.dashboard'))               

