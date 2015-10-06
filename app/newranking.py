from app import db, models

total = 0
entries = 0

WEIGHTS = [
	['binganalytics', 0.6], //BING
	['google', 0.7] //GOOGLE
]

def GETWEIGHT(METRIC):
	return weights[metric]

def addscore(score, METRIC):
	global total
	global entries

	WEIGHT = GETWEIGHT(METRIC)
	total += WEIGHT*score
	entries += WEIGHT



def Ranker(websiteurl):

	#Load in the site to be ranked
	site = models.Site.query.filter(models.Site.domainurl == websiteurl).first()
    
    #Domain ranking
	if site.binganalytics:
		addscore(1, 'binganalytics')
	else:
		addscore(-1, 'binganalytics')

	if site.googleanalytics:
		addscore(7)
	else:
		addscore(3)

	if site.robots:
		addscore(8)
	else:
		addscore(4)

	if site.sitemap:
		addscore(8)
	else:
		addscore(4)

	#List checks
	h1checklist = []
	h2checklist = []
	h3checklist = []
	alttagchecklist = []
	metadescchecklist = []
	titlechecklist = []

	#Page ranking
	for page in site.pages:

		#List checks
		h1s = page.h1s.split('#')
		for h1 in h1s:
			if h1 in h1checklist:
				addscore(6)
			else:
				addscore(4)
			h1checklist.append(h1)

		h2s = page.h2s.split('#')
		for h2 in h2s:
			if h2 in h2checklist:
				addscore(6)
			else:
				addscore(4)
			h2checklist.append(h2)

		h3s = page.h3s.split('#')
		for h3 in h3s:
			if h3 in h3checklist:
				addscore(6)
			else:
				addscore(4)
			h3checklist.append(h3)

		alttags = page.alttags.split('#')
		for alttag in alttags:
			if alttag in alttagchecklist:
				addscore(6)
			else:
				addscore(4)
			alttagchecklist.append(alttag)

		metadescs = page.metadesc.split('#')
		for metadesc in metadescs:
			if metadesc in metadescchecklist:
				addscore(6)
			else:
				addscore(4)
			metadescchecklist.append(metadesc)

		#Slightly different as there is only one title
		title = page.title
		if title in titlechecklist:
			addscore(6)
		else:
			addscore(4)
		titlechecklist.append(title)

		#Boolean checks
		if page.viewstate:
			addscore(2)

		if page.pagination:
			addscore(6)

		if page.iframe:
			addscore(4)

		if page.flash:
			addscore(3)

		if page.noindexnofollow:
			addscore(6)

		if page.schematag:
			addscore(7)

		if page.bloglocation:
			addscore(6)

		if page.internallinksno > 9:
			addscore(8)
		elif page.internallinksno > 19:
			addscore(9)

		if len(page.pageurl) < 100:
			addscore(7)
		elif len(page.pageurl) < 150:
			addscore(4)
		else:
			addscore(3)

	ranking = total / entries * 10

	site.ranking = ranking
	db.session.commit()