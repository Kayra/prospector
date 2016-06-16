from app import db


class SiteData(db.Model):

	__tablename__ = "site_data"

	id = db.Column(db.Integer, primary_key=True)
	domainurl = db.Column(db.String(300), index=True)
	sitename = db.Column(db.String(100), index=True)
	binganalytics = db.Column(db.String(10000), index=True)
	googleanalytics = db.Column(db.String(10000), index=True)
	robots = db.Column(db.String(50000))
	sitemap = db.Column(db.String(50000))
	ranking = db.Column(db.Integer)
	level = db.Column(db.Integer)

	# Establishes one to many relationship
	pages = db.relationship('PageData', backref='domain_site', lazy='dynamic')

	def __repr__(self):
		return '<SiteData %r>' % (self.domainurl)


class PageData(db.Model):

	__tablename__ = "page_data"

	id = db.Column(db.Integer, primary_key=True)
	pageurl = db.Column(db.String(500), index=True)
	h1s = db.Column(db.String(1000), index=True)
	h2s = db.Column(db.String(1000), index=True)
	h3s = db.Column(db.String(1000), index=True)
	alttags = db.Column(db.String(1000), index=True, default=False)
	metadesc = db.Column(db.String(1000), index=True)
	title = db.Column(db.String(1000), index=True)
	viewstate = db.Column(db.String(10000), index=True)
	pagination = db.Column(db.String(1000))
	iframe = db.Column(db.String(1000), default=False)
	flash = db.Column(db.String(1000), default=False)
	noindexnofollow = db.Column(db.String(1000), default=False)
	schematag = db.Column(db.String(1000), default=False)
	bloglocation = db.Column(db.String(1000), default=False)
	internallinksno = db.Column(db.Integer)

	# Establishes one to many relationship
	site_id = db.Column(db.Integer, db.ForeignKey('site_data.id'))

	def __repr__(self):
		return '<PageData %r>' % (self.pageurl)
