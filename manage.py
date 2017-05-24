import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.prospector.utils import create_default_domain_scores, create_default_page_scores

app = create_app(os.getenv("FLASK_CONFIG") or "default")

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def db_create():

    db.create_all()

    default_domain_scores = create_default_domain_scores()
    default_domain_scores.owner = None

    default_page_scores = PageScores(h1_tags=9,
                                     h2_tags=8,
                                     h3_tags=7,
                                     alt_tags=6,
                                     meta_descriptions=7,
                                     title_text=8,
                                     view_state=2,
                                     pagination=8,
                                     iframe_content=4,
                                     flash_attribute=3,
                                     no_index_no_follow_attribute=6,
                                     schema_tags=7,
                                     blog_locations=8,
                                     number_of_internal_links={
                                         "high": {
                                             19: 9
                                         },
                                         "medium": {
                                             9: 7
                                         },
                                         "low": {
                                             8: 5
                                         }
                                     },
                                     url_character_length={
                                         "high": {
                                             150: 2
                                         },
                                         "medium": {
                                             100: 4
                                         },
                                         "low": {
                                             50: 7
                                         },
                                     },
                                     owner=None)

    db.session.add(default_domain_scores)
    db.session.add(default_page_scores)
    db.session.commit()

    print("Created new database.")


if __name__ == "__main__":
    manager.run()
