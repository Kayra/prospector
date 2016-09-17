from flask import render_template, flash, redirect, url_for

from config import POSTS_PER_PAGE

from app import app, db, models
from app.forms import UrlEntry
from app.crawler import Crawler
from app.ranker import Ranker
from app.utils import format_url, extract_site_name


@app.route('/', methods=['GET', 'POST'])
def index():

    form = UrlEntry()

    if form.validate_on_submit():

        url_to_prospect = format_url(form.url.data)
        site_name = extract_site_name(url_to_prospect)

        try:
            crawler = Crawler()
            domain_data = crawler.scrape_domain_data(url_to_prospect)
            print("HIT", domain_data)

            site_id = models.DomainData.query.filter_by(site_name=site_name).first().id
            Ranker(site_id)
            return redirect(url_for('siteinspect', site_name=site_name))
        except ValueError as error:
            print(error)
            flash("Invalid url")

    return render_template("index.html", form=form)


@app.route('/sites')
def sitelist():
    sites = db.session.query(models.DomainData).limit(10)
    return render_template("sitelist.html", sites=sites)


@app.route('/site/<site_name>')
@app.route('/site/<site_name>/<int:page>')
def siteinspect(site_name, page=1):

    if site_name is None:
        return redirect(url_for('index'))

    site = db.session.query(models.DomainData).filter_by(site_name=site_name).first()

    currentPages = models.PageData.query.filter_by(site_id=site.id).paginate(page, POSTS_PER_PAGE, False)

    return render_template("siteinspect.html", site=site, currentPages=currentPages)
