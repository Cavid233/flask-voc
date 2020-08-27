from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

go_b = Blueprint('go', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db



@go_b.route("/go_1/<string:title>/<string:kind>")
def go_1(kind,title):
    if kind == 'A1':
        create_number = Create.query.filter_by(title = title).first()
        return redirect(url_for('levels.test',id=create_number.id))

    elif kind == 'A2':
        create_number = A2.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_A2',id=create_number.id))

    elif kind == 'B1':
        create_number = B1.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_B1',id=create_number.id))

    elif kind == 'B2':
        create_number = B2.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_B2',id=create_number.id))
        
    else:    
        create_number = Ielts_words.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_IE',id=create_number.id))


@go_b.route("/go_2/<string:title>/<string:kind>")
@login_required
def go_2(kind,title):
    if kind == 'A1':
        create_number = Create.query.filter_by(title = title).first()
        return redirect(url_for('levels.test',id=create_number.id))

    elif kind == 'A2':
        create_number = A2.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_A2',id=create_number.id))

    elif kind == 'B1':
        create_number = B1.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_B1',id=create_number.id))

    elif kind == 'B2':
        create_number = B2.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_B2',id=create_number.id))
            
    else:    
        create_number = Ielts_words.query.filter_by(title = title).first()
        return redirect(url_for('levels.test_IE',id=create_number.id))


@go_b.route("/go_3/<string:title>")
@login_required
def go_3(title):
    create_number = Create.query.filter_by(title = title).first()
    return redirect(url_for('levels.test',id=create_number.id))