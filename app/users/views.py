from flask import Blueprint

users_blueprint = Blueprint('users', __name__)

@app.route('/login')
def login():
    pass

@app.route('/logout')
def logout():
    pass

@app.route('/profile/<username>')
@login_required
def profile(username):
    pass
