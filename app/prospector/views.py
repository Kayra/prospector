from flask import current_app, Blueprint, render_template, redirect, url_for

from app.prospector.models import DomainData, PageData, db
from app.prospector.forms import UrlEntry
from app.prospector.crawler import Crawler
from app.prospector.ranker import Ranker
from app.prospector.utils import format_url


prospector_blueprint = Blueprint('prospector', __name__)


@prospector_blueprint.route('/', methods=['GET', 'POST'])
def index():

    form = UrlEntry()

    if form.validate_on_submit():

        url_to_prospect = format_url(form.url.data)

        crawler = Crawler()

        domain_data = crawler.scrape_domain_data(url_to_prospect)

        pages_to_scrape = crawler.spider_site(domain_data.domain_url)
        pages_data = [crawler.scrape_page_data(page_to_scrape, domain_data) for page_to_scrape in pages_to_scrape]

        ranker = Ranker()
        domain_data.ranking = ranker.rank_site(domain_data)
        domain_data.level = ranker.domain_level_calculator(domain_data.ranking)

        db.session.add(domain_data)
        db.session.add_all(pages_data)
        db.session.commit()

        return redirect(url_for('siteinspect', site_name=domain_data.site_name))

    return render_template("index.html", form=form)


@prospector_blueprint.route('/sites')
def sitelist():
    sites_per_page = current_app.config["SITES_PER_PAGE"]
    sites = db.session.query(DomainData).limit(sites_per_page)
    return render_template("sitelist.html", sites=sites)


@prospector_blueprint.route('/site/<site_name>')
@prospector_blueprint.route('/site/<site_name>/<int:page>')
def siteinspect(site_name, page=1):

    if site_name is None:
        return redirect(url_for('index'))

    site = db.session.query(DomainData).filter_by(site_name=site_name).first()

    currentPages = PageData.query.filter_by(site_id=site.id).paginate(page, 1, False)

    return render_template("siteinspect.html", site=site, currentPages=currentPages)
