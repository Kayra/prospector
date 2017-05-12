from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_user import UserMixin

from app import login_manager, db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError("The password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def confirm(self, token):

        serializer = Serializer(current_app.config["SECRET_KEY"])

        try:
            data = serializer.loads(token)
        except Exception as exception:
            print(exception)
            return False

        if data.get("confirm") == self.id:
            self.confirmed = True
            db.session.add(self)
            db.session.commit()
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % (self.username)
