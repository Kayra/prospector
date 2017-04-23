from flask import Blueprint, render_template, flash, redirect, url_for
from flask_user import login_required

from app import db
from app.users.forms import LoginForm, RegistrationForm
from app.users.models import User

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/register', methods=["GET", "POST"])
def register():

    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():

        user = User(email=registration_form.email.data,
                    username=registration_form.username.data,
                    password=registration_form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Your account has been created. Please log in.")

        return redirect(url_for("users.login"))

    else:
        return render_template("users/register.html", form=registration_form)


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

