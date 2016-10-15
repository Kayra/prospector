from flask import render_template, redirect, url_for

from config import SITES_PER_PAGE

from app import app, db, models
from app.forms import UrlEntry
from app.crawler import Crawler
from app.ranker import Ranker
from app.utils import format_url


@app.route('/', methods=['GET', 'POST'])
def index():

    form = UrlEntry()

    if form.validate_on_submit():

        url_to_prospect = format_url(form.url.data)

        domain_data = models.DomainData.query.filter_by(domain_url=url_to_prospect).first()

        if domain_data:
            domain_data = Crawler.scrape_domain_data(url_to_prospect, domain_data)
        else:
            domain_data = Crawler.scrape_domain_data(url_to_prospect)

        pages_to_scrape = Crawler.spider_site(domain_data.domain_url)
        pages_data = [Crawler.scrape_page_data(page_to_scrape, domain_data) for page_to_scrape in pages_to_scrape]

        ranker = Ranker()
        domain_data.ranking = ranker.rank_site(domain_data)
        domain_data.level = ranker.domain_level_calculator(domain_data.ranking)

        db.session.add(domain_data)
        db.session.add_all(pages_data)
        db.session.commit()

        return redirect(url_for('siteinspect', site_name=domain_data.site_name))

    return render_template("index.html", form=form)


@app.route('/sites')
def sitelist():
    sites = db.session.query(models.DomainData).limit(SITES_PER_PAGE)
    return render_template("sitelist.html", sites=sites)


@app.route('/site/<site_name>')
@app.route('/site/<site_name>/<int:page>')
def siteinspect(site_name, page=1):

    if site_name is None:
        return redirect(url_for('index'))

    site = db.session.query(models.DomainData).filter_by(site_name=site_name).first()

    currentPages = models.PageData.query.filter_by(site_id=site.id).paginate(page, 1, False)

    return render_template("siteinspect.html", site=site, currentPages=currentPages)
