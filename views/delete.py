from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

delete_b = Blueprint('delete', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db,Corrects


@delete_b.route('/delete_1/<int:id>')
@login_required
def delete_1(id):
    delete_1 = Punctuation_1.query.filter_by(id = id,author=session['username']).first()

    if delete_1:
        db.session.delete(delete_1)

        db.session.commit()
 
        return redirect(url_for('out.out_exclamation'))   
    else:
        flash('Unable To Delete','danger')
        return redirect(url_for('out.out_exclamation'))

@delete_b.route('/delete_2/<int:id>')
def delete_2(id):
    delete_2 = Punctuation_2.query.filter_by(id = id,author=session['username']).first()

    if delete_2:

        db.session.delete(delete_2)

        db.session.commit()
 
        return redirect(url_for('out.out_question_circle'))    
    else:
        flash('Unable To Delete','danger')
        return redirect(url_for('out.out_question_circle'))  


@delete_b.route('/delete_3/<int:id>')
def delete_3(id):
    delete_3 = Corrects.query.filter_by(id = id,author=session['username']).first()

    if delete_3:

        db.session.delete(delete_3)

        db.session.commit()
 
        return redirect(url_for('correct.correct_1'))    
    else:
        flash('Unable To Delete','danger')
        return redirect(url_for('correct.correct_1'))  