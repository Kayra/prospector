import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Pagination
SITES_PER_PAGE = 1

# Ranking calculation constant
DOMAIN_IMPORTANCE = 1.3

# Spidering limit
MAX_PAGES_TO_VISIT = 60

# Don't need for this application, if user accounts are added in the future this will be useful
CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'
