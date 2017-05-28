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


class PageScoresForm(FlaskForm):

    h1_tags = IntegerField('h1_tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    h2_tags = IntegerField('h2_tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    h3_tags = IntegerField('h3_tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    alt_tags = IntegerField('alt_tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    meta_descriptions = IntegerField('meta_descriptions', validators=[DataRequired(), NumberRange(min=1, max=10)])
    title_text = IntegerField('title_text', validators=[DataRequired(), NumberRange(min=1, max=10)])
    view_state = IntegerField('view_state', validators=[DataRequired(), NumberRange(min=1, max=10)])
    pagination = IntegerField('pagination', validators=[DataRequired(), NumberRange(min=1, max=10)])
    iframe_content = IntegerField('iframe_content', validators=[DataRequired(), NumberRange(min=1, max=10)])
    flash_attribute = IntegerField('flash_attribute', validators=[DataRequired(), NumberRange(min=1, max=10)])
    no_index_no_follow_attribute = IntegerField('no_index_no_follow_attribute', validators=[DataRequired(), NumberRange(min=1, max=10)])
    schema_tags = IntegerField('schema_tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    blog_locations = IntegerField('blog_locations', validators=[DataRequired(), NumberRange(min=1, max=10)])
