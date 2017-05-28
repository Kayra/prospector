from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class UrlEntry(FlaskForm):
    url = StringField('url', validators=[DataRequired()])


class DomainScoresForm(FlaskForm):

    google_analytics = IntegerField('google_analytics', validators=[DataRequired(), NumberRange(min=1, max=10)])
    bing_analytics = IntegerField('bing_analytics', validators=[DataRequired(), NumberRange(min=1, max=10)])
    robots_txt = IntegerField('robots_txt', validators=[DataRequired(), NumberRange(min=1, max=10)])
    sitemap_xml = IntegerField('sitemap_xml', validators=[DataRequired(), NumberRange(min=1, max=10)])

    submit = SubmitField("Save")
