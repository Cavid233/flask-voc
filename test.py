from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_ckeditor import CKEditor

from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



############################################################
from views.log_reg import log_reg
from views.correct import correct_b
from views.levels import levels_b
from views.go import go_b
from views.search import search_b
from views.delete import delete_b
from views.dash_fil import dash_fil_b
from views.out import out_b
from views.punc import punc_b
from views.create import create_b
from views.update import update_b
from views.index import index_b
from views.logout import logout_b



#####################################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users\Cavid\Desktop\Voc\datas.db'
app.config['DEBUG']=True
ckeditor = CKEditor(app)



db = SQLAlchemy(app)
app.secret_key='word'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)



 
############### Test #############################
app.register_blueprint(log_reg)
app.register_blueprint(correct_b)
app.register_blueprint(levels_b)
app.register_blueprint(go_b)
app.register_blueprint(search_b)
app.register_blueprint(delete_b)
app.register_blueprint(dash_fil_b)
app.register_blueprint(out_b)
app.register_blueprint(punc_b)
app.register_blueprint(create_b)
app.register_blueprint(update_b)
app.register_blueprint(index_b)
app.register_blueprint(logout_b)






if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

