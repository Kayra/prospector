from flask import Blueprint, app
from flask_user import login_required

users_blueprint = Blueprint('users', __name__)


@app.route('/login')
def login():
    print("HIT LOGIN")
    pass


@app.route('/logout')
def logout():
    print("HIT LOGOUT")
    pass


@app.route('/profile/<username>')
@login_required
def profile(username):
    print("HIT PROFILE ON USER", username)
    pass
