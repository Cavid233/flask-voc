from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

search_b = Blueprint('search', __name__)

from .models import Punctuation_1,Punctuation_2,Create,login_required,A2,B1,B2,Ielts_words,db,Corrects


# Arama URL

@search_b.route('/find',methods=['POST','GET'])
@login_required
def find():
    keyword = request.form.get('keyword')
    if keyword.isnumeric():
        if session['kind'] == 'A1':
            return redirect(url_for('levels.test',id= keyword))
        elif session['kind'] == 'A2':
            return redirect(url_for('levels.test_A2',id= keyword))
        elif session['kind'] == 'B1':
            return redirect(url_for('levels.test_B1',id= keyword))
        elif session['kind'] == 'B2':
            return redirect(url_for('levels.test_B2',id= keyword))
        elif session['kind'] == 'IE':
            return redirect(url_for('levels.test_IE',id= keyword))
    else:
        flash('Please try again','warning')
        return redirect(url_for('index.index'))    


@search_b.route('/search',methods=['POST','GET'])
@login_required
def search():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        keyword = request.form.get('keyword')  

        search ="{}%".format(keyword)
        
        posts = Create.query.filter(Create.title.like(search)).filter_by(author = session['username']).all()

        s_A1 = Create.query.filter(Create.title.like(search)).filter_by(author = 'everyone').all()
        s_A2 = A2.query.filter(A2.title.like(search)).filter_by(author = 'everyone').all()
        s_B1 = B1.query.filter(B1.title.like(search)).filter_by(author = 'everyone').all()
        s_B2 = B2.query.filter(B2.title.like(search)).filter_by(author = 'everyone').all()
        s_IE = Ielts_words.query.filter(Ielts_words.title.like(search)).filter_by(author = 'everyone').all()

        mars = posts+s_A1+s_A2+s_B1+s_B2+s_IE
        if mars:

            return render_template('dashboard.html',mars = mars)  
        else:
            flash('No suitable questions found','warning')
            return redirect(url_for('dash_fil.dashboard'))
    

# Arama URL
@search_b.route('/ex_search',methods=['POST','GET'])
@login_required
def ex_search():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        keyword = request.form.get('ex_keyword') 

        search ="{}%".format(keyword)

        posts_1 = Punctuation_1.query.filter(Punctuation_1.title.like(search)).filter_by(author = session['username']).all()
        
        posts = posts_1 
        if posts:

            return render_template('exclamation.html',posts = posts)  
        else:
            flash('No suitable questions found','warning')
            return redirect(url_for('out.out_exclamation'))            


# Arama URL
@search_b.route('/qu_search',methods=['POST','GET'])
@login_required
def qu_search():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        keyword = request.form.get('qu_keyword') 

        search ="{}%".format(keyword)

        posts_1 = Punctuation_2.query.filter(Punctuation_2.title.like(search)).filter_by(author = session['username']).all()

        sends = posts_1

        if sends:
            return render_template('question_circle.html',sends = sends)  
        else:
            flash('No suitable questions found','warning')
            return redirect(url_for('out.out_question_circle')) 



# Arama URL
@search_b.route('/co_search',methods=['POST','GET'])
@login_required
def co_search():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        keyword = request.form.get('qu_keyword') 

        search ="{}%".format(keyword)

        posts_1 = Corrects.query.filter(Corrects.title.like(search)).filter_by(author = session['username']).all()

        gives = posts_1

        if gives:
            return render_template('correct.html',gives = gives)  
        else:
            flash('No suitable questions found','warning')
            return redirect(url_for('correct.correct_1')) 
