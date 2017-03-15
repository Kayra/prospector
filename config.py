import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://prospector:password@localhost:5432/prospector'
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


class Configuration:

    SECRET_KEY = os.environ.get("SECRET_KEY") or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination
    SITES_PER_PAGE = 1

    # Ranking calculation constant
    DOMAIN_IMPORTANCE = 1.3

    # Spidering limit
    MAX_PAGES_TO_VISIT = 60

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfigruation(Configuration):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or "postgresql://prospector:password@localhost:5432/prospector"
    SQLALCHEMY_MIGRATE_REPO = os.environ.get("DEV_DB_REPOSITORY_URL") or os.path.join(basedir, 'db_repository')
