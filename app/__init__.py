from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)
user_manager = UserManager(db, app)

from app.prospector.views import prospector_blueprint
app.register_blueprint(prospector_blueprint)

from app.users.views import users_blueprint
app.register_blueprint(users_blueprint)

from app.prospector import views, models
