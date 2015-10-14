from flask import render_template, flash, redirect, url_for
from app import app, db, models
from .forms import UrlEntry
from .crawler import Crawler
from .ranker import Ranker


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    form = UrlEntry()

    # If a url has been entered, assess the website and redirect to the page displaying the results
    if form.validate_on_submit():
        domainname = Crawler(form.url.data)  # Introducing a dependency, not a strong dependency
        Ranker(form.url.data)
        return redirect(url_for('siteinspect', sitename=domainname))

    # If this is the first time the user is visiting the page (i.e. nothing has been submitted) simply load the template and form
    return render_template("index.html", form=form)


@app.route('/sitelist')
def sitelist():

    # Get the latest 10 websites
    sites = db.session.query(models.Site).limit(10)
    return render_template("sitelist.html", sites=sites)


@app.route('/siteinspect/<sitename>')
@app.route('/siteinspect/<sitename>/<int:page>')
def siteinspect(sitename, page=1):

    if sitename is None:
        flash("That site doesn't seem to exist")
        return redirect(url_for('index'))

    site = db.session.query(models.Site).filter_by(sitename=sitename).first()

    currentPages = models.Page.query.filter_by(siteid=site.id).paginate(page, 1, False)

    return render_template("siteinspect.html", site=site, currentPages=currentPages)
