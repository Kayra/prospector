import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.prospector.utils import create_default_domain_scores, create_default_page_scores

app = create_app()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def db_create():

    db.create_all()

    default_domain_scores = create_default_domain_scores()
    default_page_scores = create_default_page_scores()

    db.session.add(default_domain_scores)
    db.session.add(default_page_scores)
    db.session.commit()

    print("Created new database.")


if __name__ == "__main__":
    manager.run()
