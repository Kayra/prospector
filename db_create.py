#!/usr/bin/env python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
from app.models import DomainScores, PageScores
import os.path

db.create_all()

default_domain_scores = DomainScores(google_analytics=9,
                                     bing_analytics=8,
                                     robots_txt=9,
                                     sitemap_xml=9)


default_page_scores = PageScores(h1_tags=9,
                                 h2_tags=8,
                                 h3_tags=7,
                                 alt_tags=6,
                                 meta_description=7,
                                 title_text=8,
                                 view_state=2,
                                 pagination=8,
                                 iframe_content=4,
                                 flash_attribute=3,
                                 no_index_no_follow_attribute=6,
                                 schema_tag=7,
                                 blog_location=8,
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
                                     }
                                 })


db.session.add(default_domain_scores)
db.session.add(default_page_scores)
db.session.commit()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
