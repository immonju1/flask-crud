from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_ECHO"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///juhawsgi'


db = SQLAlchemy(app)

from application import views

from application.tasks import models
from application.tasks import views

from application.auth import models
from application.auth import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# luodaan taulut tietokantaan tarvittaessa
db.create_all()

def sql(rawSql, sqlVars={}):
    assert type(rawSql)==str
    assert type(sqlVars)==dict
    res=db.session.execute(rawSql, sqlVars)
    db.session.commit()
    return res

@app.before_first_request
def initDBforFlask():
    sql("insert into account(name, username, password) values ('JI','ji','mono');")


