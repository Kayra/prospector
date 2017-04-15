from flask import Blueprint, render_template
from flask_user import login_required

from app.users.forms import LoginForm

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login')
def login():

    login_form = LoginForm()

    return render_template("users/login.html", form=login_form)


@users_blueprint.route('/logout')
def logout():
    print("HIT LOGOUT")
    pass


@users_blueprint.route('/profile/<username>')
@login_required
def profile(username):
    print("HIT PROFILE ON USER", username)
    pass


@users_blueprint.route('/register')
def register():
    print("HIT")
    return("HIT")
