from flask import Blueprint,Flask,render_template,redirect,url_for,request,flash,session,logging

logout_b = Blueprint('logout', __name__)


#Logout islemi 
@logout_b.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('log_reg.login'))