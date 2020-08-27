from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging
from passlib.hash import sha256_crypt

log_reg = Blueprint('log_reg', __name__)

from .models import Register, db


@log_reg.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username= request.form.get('l_username')
        password= request.form.get('l_password')

        l_users = Register.query.filter_by(username = username).first()
        if l_users:
            if sha256_crypt.verify(password,l_users.password):
                flash('You have successfully logged in','success')

                session['logged_in']=True
                session['username']=username
                session['correct']=0

                return redirect(url_for('levels.test',id=1)) 
            else:
                flash("You have entered your password incorrectly",'danger')
                return redirect(url_for('log_reg.login'))
        else:
            flash("No such user or username isn't correct",'danger')
            return redirect(url_for('log_reg.login'))    

    return render_template('login.html')



@log_reg.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        r_password = request.form.get('r_password')

        exist_username = Register.query.filter_by(username = username).first()

        exist_email = Register.query.filter_by(email = email).first()

        if password == r_password:
            if not  exist_email :

                if not exist_username:

                    newUser = Register(name = name, username = username, email = email, password = sha256_crypt.encrypt(password))
                    db.session.add(newUser)
                    db.session.commit()    

                    return redirect(url_for('log_reg.login'))
                else:
                    flash('Try another username','danger')
                    return render_template('register.html')   
            else:
                flash('Try another email','danger')
                return render_template('register.html')   
        else:
                flash('Passwords do not match','danger')
                return render_template('register.html')                    
    else:            
        return render_template('register.html')
