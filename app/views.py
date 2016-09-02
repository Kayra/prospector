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

        try:
            Crawler(url_to_prospect)
            Ranker(url_to_prospect)
            return redirect(url_for('siteinspect', sitename=extract_site_name(url_to_prospect)))
        except ValueError as error:
            print(error)
            flash("Invalid url")

    return render_template("index.html", form=form)


@app.route('/sites')
def sitelist():
    sites = db.session.query(models.Site).limit(10)
    return render_template("sitelist.html", sites=sites)


@app.route('/site/<sitename>')
@app.route('/site/<sitename>/<int:page>')
def siteinspect(sitename, page=1):

    if sitename is None:
        return redirect(url_for('index'))

    site = db.session.query(models.Site).filter_by(sitename=sitename).first()

    currentPages = models.Page.query.filter_by(siteid=site.id).paginate(page, POSTS_PER_PAGE, False)

    return render_template("siteinspect.html", site=site, currentPages=currentPages)
