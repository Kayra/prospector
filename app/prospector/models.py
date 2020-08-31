from uuid import uuid4

from sqlalchemy.dialects.postgresql import JSON, ARRAY, UUID

from app import db


class DomainData(db.Model):

	__tablename__ = "domain_data"

	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
	domain_url = db.Column(db.String(300), index=True)
	site_name = db.Column(db.String(100), index=True)
	bing_analytics = db.Column(db.String(10000), index=True)
	google_analytics = db.Column(db.String(10000), index=True)
	robots_txt = db.Column(db.String(50000))
	sitemap_xml = db.Column(db.String(50000))
	ranking = db.Column(db.Integer, default=0)
	level = db.Column(db.String(6))

	pages = db.relationship('PageData', backref='domain_site', lazy='dynamic')

	owner = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)

	def __repr__(self):
		return '<DomainData %r>' % (self.site_name)


class PageData(db.Model):

	__tablename__ = "page_data"

	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
	page_url = db.Column(db.String(500), index=True)
	h1_tags = db.Column(ARRAY(db.String(1000)))
	h2_tags = db.Column(ARRAY(db.String(1000)))
	h3_tags = db.Column(ARRAY(db.String(1000)))
	alt_tags = db.Column(ARRAY(db.String(1000)))
	meta_descriptions = db.Column(ARRAY(db.String(1000)))
	title_text = db.Column(db.String(1000), index=True)
	view_state = db.Column(db.String(10000), index=True)
	pagination = db.Column(db.String(1000))
	iframe_content = db.Column(db.String(1000), default=False)
	flash_attribute = db.Column(db.String(1000), default=False)
	no_index_no_follow_attribute = db.Column(db.String(1000), default=False)
	schema_tags = db.Column(ARRAY(db.String(10000)))
	blog_locations = db.Column(ARRAY(db.String(1000)))
	number_of_internal_links = db.Column(db.Integer)

	site_id = db.Column(UUID(as_uuid=True), db.ForeignKey('domain_data.id'), nullable=False)

	def __repr__(self):
		return '<PageData %r>' % (self.page_url)


class DomainScores(db.Model):

	__tablename__ = "domain_scores"

	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
	google_analytics = db.Column(db.Integer)
	bing_analytics = db.Column(db.Integer)
	robots_txt = db.Column(db.Integer)
	sitemap_xml = db.Column(db.Integer)

	owner = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)

	def __repr__(self):
		return '<DomainScores>'


class PageScores(db.Model):

	__tablename__ = "page_scores"

	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
	h1_tags = db.Column(db.Integer)
	h2_tags = db.Column(db.Integer)
	h3_tags = db.Column(db.Integer)
	alt_tags = db.Column(db.Integer)
	meta_descriptions = db.Column(db.Integer)
	title_text = db.Column(db.Integer)
	view_state = db.Column(db.Integer)
	pagination = db.Column(db.Integer)
	iframe_content = db.Column(db.Integer)
	flash_attribute = db.Column(db.Integer)
	no_index_no_follow_attribute = db.Column(db.Integer)
	schema_tags = db.Column(db.Integer)
	blog_locations = db.Column(db.Integer)
	number_of_internal_links = db.Column(JSON)
	url_character_length = db.Column(JSON)

	owner = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=True)

	def __repr__(self):
		return '<PageScores>'
