#Don't need for this application, if user accounts are added in the future this needs to be re-enabled
CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#pagination
POSTS_PER_PAGE = 1
