from app import db


class DomainData(db.Model):

	__tablename__ = "domain_data"

	id = db.Column(db.Integer, primary_key=True)
	domain_url = db.Column(db.String(300), index=True)
	site_name = db.Column(db.String(100), index=True)
	bing_analytics = db.Column(db.String(10000), index=True)
	google_analytics = db.Column(db.String(10000), index=True)
	robots = db.Column(db.String(50000))
	sitemap = db.Column(db.String(50000))
	ranking = db.Column(db.Integer, default=0)
	level = db.Column(db.Integer)

	pages = db.relationship('PageData', backref='domain_site', lazy='dynamic')

	def __repr__(self):
		return '<DomainData %r>' % (self.domain_url)


class PageData(db.Model):

	__tablename__ = "page_data"

	id = db.Column(db.Integer, primary_key=True)
	page_url = db.Column(db.String(500), index=True)
	h1s = db.Column(db.String(1000), index=True)
	h2s = db.Column(db.String(1000), index=True)
	h3s = db.Column(db.String(1000), index=True)
	alt_tags = db.Column(db.String(1000), index=True, default=False)
	meta_desc = db.Column(db.String(1000), index=True)
	title = db.Column(db.String(1000), index=True)
	view_state = db.Column(db.String(10000), index=True)
	pagination = db.Column(db.String(1000))
	iframe = db.Column(db.String(1000), default=False)
	flash = db.Column(db.String(1000), default=False)
	no_index_no_follow = db.Column(db.String(1000), default=False)
	schema_tag = db.Column(db.String(1000), default=False)
	blog_location = db.Column(db.String(1000), default=False)
	number_of_internal_links = db.Column(db.Integer)

	site_id = db.Column(db.Integer, db.ForeignKey('domain_data.id'))

	def __repr__(self):
		return '<PageData %r>' % (self.page_url)
