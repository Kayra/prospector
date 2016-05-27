from flask import render_template, flash, redirect, url_for
from app import app, db, models
from .forms import UrlEntry
from .crawler import Crawler
from .ranker import Ranker


@app.route('/', methods=['GET', 'POST'])
def index():

    form = UrlEntry()

    if form.validate_on_submit():

        url_to_prospect = form.url.data

        if 'www.' not in url_to_prospect and 'http://' not in url_to_prospect:
            url_to_prospect = 'http://www.' + url_to_prospect
        if 'http://' not in url_to_prospect:
            url_to_prospect = 'http://' + url_to_prospect

        try:
            domainname = Crawler(url_to_prospect)
            Ranker(url_to_prospect)
            return redirect(url_for('siteinspect', sitename=domainname))
        except ValueError:
            flash("Invalid url")

    return render_template("index.html", form=form)


@app.route('/sitelist')
def sitelist():
    sites = db.session.query(models.Site).limit(10)
    return render_template("sitelist.html", sites=sites)


@app.route('/siteinspect/<sitename>')
@app.route('/siteinspect/<sitename>/<int:page>')
def siteinspect(sitename, page=1):

    if sitename is None:
        return redirect(url_for('index'))

    site = db.session.query(models.Site).filter_by(sitename=sitename).first()

    currentPages = models.Page.query.filter_by(siteid=site.id).paginate(page, 1, False)

    return render_template("siteinspect.html", site=site, currentPages=currentPages)
