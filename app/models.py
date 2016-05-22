from app import db


class Site(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	domainurl = db.Column(db.String(300), index=True)
	sitename = db.Column(db.String(100), index=True)
	binganalytics = db.Column(db.String(10000), index=True)
	googleanalytics = db.Column(db.String(10000), index=True)
	robots = db.Column(db.String(50000))
	sitemap = db.Column(db.String(50000))
	ranking = db.Column(db.Integer)

	# Establishes one to many relationship
	pages = db.relationship('Page', backref='domainsite', lazy='dynamic')

	def __repr__(self):
		return '<Site %r>' % (self.domainurl)


class Page(db.Model):
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
	siteid = db.Column(db.Integer, db.ForeignKey('site.id'))

	def __repr__(self):
		return '<Page %r>' % (self.pageurl)
