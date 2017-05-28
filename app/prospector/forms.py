from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class UrlEntry(FlaskForm):
    url = StringField('url', validators=[DataRequired()])


class DomainScores(FlaskForm):

    google_analytics = IntegerField('google_analytics', validators=[DataRequired()])

    submit = SubmitField("Save")
    # google_analytics = db.Column(db.Integer)
    # bing_analytics = db.Column(db.Integer)
    # robots_txt = db.Column(db.Integer)
    # sitemap_xml = db.Column(db.Integer)
