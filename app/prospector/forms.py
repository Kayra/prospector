from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class UrlEntry(FlaskForm):
    url = StringField('url', validators=[DataRequired()])


class DomainScoresForm(FlaskForm):

    google_analytics = IntegerField('google_analytics', validators=[DataRequired()])
    bing_analytics = IntegerField('bing_analytics', validators=[DataRequired()])
    robots_txt = IntegerField('robots_txt', validators=[DataRequired()])
    sitemap_xml = IntegerField('sitemap_xml', validators=[DataRequired()])

    submit = SubmitField("Save")
