from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user

from app import db
from app.users.forms import LoginForm, RegistrationForm
from app.users.models import User
from app.prospector.models import DomainScores, PageScores
from app.prospector.forms import DomainScoresForm, PageScoresForm
from app.prospector.utils import create_default_domain_scores, create_default_page_scores


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

    domain_scores = DomainScores.query.filter_by(owner=user.id).first()
    domain_scores_form = DomainScoresForm()

    page_scores = PageScores.query.filter_by(owner=user.id).first()
    page_scores_form = PageScoresForm()

    if domain_scores_form.validate_on_submit():

        domain_scores.google_analytics = domain_scores_form.google_analytics.data
        domain_scores.bing_analytics = domain_scores_form.bing_analytics.data
        domain_scores.robots_txt = domain_scores_form.robots_txt.data
        domain_scores.sitemap_xml = domain_scores_form.sitemap_xml.data

        page_scores.h1_tags = page_scores_form.h1_tags.data
        page_scores.h2_tags = page_scores_form.h2_tags.data
        page_scores.h3_tags = page_scores_form.h3_tags.data
        page_scores.alt_tags = page_scores_form.alt_tags.data
        page_scores.meta_descriptions = page_scores_form.meta_descriptions.data
        page_scores.title_text = page_scores_form.title_text.data
        page_scores.view_state = page_scores_form.view_state.data
        page_scores.pagination = page_scores_form.pagination.data
        page_scores.iframe_content = page_scores_form.iframe_content.data
        page_scores.flash_attribute = page_scores_form.flash_attribute.data
        page_scores.no_index_no_follow_attribute = page_scores_form.no_index_no_follow_attribute.data
        page_scores.schema_tags = page_scores_form.schema_tags.data
        page_scores.blog_locations = page_scores_form.blog_locations.data

        db.session.add(domain_scores)
        db.session.add(page_scores)
        db.session.commit()

    domain_scores_form.google_analytics.data = domain_scores.google_analytics
    domain_scores_form.bing_analytics.data = domain_scores.bing_analytics
    domain_scores_form.robots_txt.data = domain_scores.robots_txt
    domain_scores_form.sitemap_xml.data = domain_scores.sitemap_xml

    page_scores_form.h1_tags.data = page_scores.h1_tags
    page_scores_form.h2_tags.data = page_scores.h2_tags
    page_scores_form.h3_tags.data = page_scores.h3_tags
    page_scores_form.alt_tags.data = page_scores.alt_tags
    page_scores_form.meta_descriptions.data = page_scores.meta_descriptions
    page_scores_form.title_text.data = page_scores.title_text
    page_scores_form.view_state.data = page_scores.view_state
    page_scores_form.pagination.data = page_scores.pagination
    page_scores_form.iframe_content.data = page_scores.iframe_content
    page_scores_form.flash_attribute.data = page_scores.flash_attribute
    page_scores_form.no_index_no_follow_attribute.data = page_scores.no_index_no_follow_attribute
    page_scores_form.schema_tags.data = page_scores.schema_tags
    page_scores_form.blog_locations.data = page_scores.blog_locations

    return render_template("users/profile.html", user=user, domain_scores_form=domain_scores_form, page_scores_form=page_scores_form)


@users_blueprint.route('/domain_scores/<username>', methods=["GET", "POST"])
@login_required
def edit_domain_scores(username):

    user = User.query.filter_by(username=username).first()

    domain_scores = DomainScores.query.filter_by(owner=user.id).first()
    domain_scores_form = DomainScoresForm()

    if domain_scores_form.validate_on_submit():

        domain_scores.google_analytics = domain_scores_form.google_analytics.data
        domain_scores.bing_analytics = domain_scores_form.bing_analytics.data
        domain_scores.robots_txt = domain_scores_form.robots_txt.data
        domain_scores.sitemap_xml = domain_scores_form.sitemap_xml.data

        db.session.add(domain_scores)
        db.session.commit()
        flash("Your domain scores have been updated.")

    domain_scores_form.google_analytics.data = domain_scores.google_analytics
    domain_scores_form.bing_analytics.data = domain_scores.bing_analytics
    domain_scores_form.robots_txt.data = domain_scores.robots_txt
    domain_scores_form.sitemap_xml.data = domain_scores.sitemap_xml

    return render_template("users/edit_domain_scores.html", user=user, domain_scores_form=domain_scores_form)
