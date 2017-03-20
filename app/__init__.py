from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from config import configurations

db = SQLAlchemy()
mail = Mail()


def create_app(configuration_name):

    app = Flask(__name__)
    app.config.from_object(configurations[configuration_name])
    configurations[configuration_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)

    from app.prospector.views import prospector_blueprint
    app.register_blueprint(prospector_blueprint)

    from app.users.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app
