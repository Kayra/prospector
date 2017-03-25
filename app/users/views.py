from flask import Blueprint
from flask_user import login_required

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login')
def login():
    print("HIT LOGIN")
    pass


@users_blueprint.route('/logout')
def logout():
    print("HIT LOGOUT")
    pass


@users_blueprint.route('/profile/<username>')
@login_required
def profile(username):
    print("HIT PROFILE ON USER", username)
    pass
