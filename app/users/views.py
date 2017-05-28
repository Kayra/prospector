from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user

from app import db
from app.users.forms import LoginForm, RegistrationForm
from app.users.models import User
from app.prospector.models import DomainScores, PageScores
from app.prospector.forms import DomainScoresForm, PageScoresForm
from app.prospector.utils import (create_default_domain_scores, create_default_page_scores, load_domain_scores_form_to_model,
                                  load_domain_scores_model_to_form, load_page_scores_form_to_model, load_page_scores_model_to_form)


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

        default_domain_scores = create_default_domain_scores(owner=user.id)
        default_page_scores = create_default_page_scores(owner=user.id)

        db.session.add(default_domain_scores)
        db.session.add(default_page_scores)
        db.session.commit()

        flash("Your account has been created. Please log in.")

        return redirect(url_for("users.login"))

    else:
        return render_template("users/register.html", form=registration_form)


@users_blueprint.route('/login', methods=["GET", "POST"])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():

        user = User.query.filter_by(email=login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember_me.data)
            return redirect(request.args.get("next") or url_for("prospector.index"))

        else:
            flash("Invalid username or password")

    return render_template("users/login.html", form=login_form)


@users_blueprint.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("prospector.index"))


@users_blueprint.route('/profile/<username>', methods=["GET", "POST"])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template("users/profile.html", user=user)


@users_blueprint.route('/domain_scores/<username>', methods=["GET", "POST"])
@login_required
def edit_domain_scores(username):

    user = User.query.filter_by(username=username).first()

    domain_scores_model = DomainScores.query.filter_by(owner=user.id).first()
    domain_scores_form = DomainScoresForm()

    if domain_scores_form.validate_on_submit():

        domain_scores_model = load_domain_scores_form_to_model(domain_scores_model, domain_scores_form)

        db.session.add(domain_scores_model)
        db.session.commit()
        flash("Your domain scores have been updated.")

    domain_scores_form = load_domain_scores_model_to_form(domain_scores_model, domain_scores_form)

    return render_template("users/edit_domain_scores.html", user=user, domain_scores_form=domain_scores_form)


@users_blueprint.route('/page_scores/<username>', methods=["GET", "POST"])
@login_required
def edit_page_scores(username):

    user = User.query.filter_by(username=username).first()

    page_scores = PageScores.query.filter_by(owner=user.id).first()
    page_scores_form = PageScoresForm()

    if page_scores_form.validate_on_submit():

        page_scores = load_page_scores_form_to_model(page_scores, page_scores_form)

        db.session.add(page_scores)
        db.session.commit()
        flash("Your page scores have been updated.")

    page_scores_form = load_page_scores_model_to_form(page_scores, page_scores_form)

    return render_template("users/edit_page_scores.html", user=user, page_scores_form=page_scores_form)
