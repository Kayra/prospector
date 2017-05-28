from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class UrlEntry(FlaskForm):
    url = StringField('url', validators=[DataRequired()])


class DomainScoresForm(FlaskForm):

    google_analytics = IntegerField('Google Analytics', validators=[DataRequired(), NumberRange(min=1, max=10)])
    bing_analytics = IntegerField('Bing Analytics', validators=[DataRequired(), NumberRange(min=1, max=10)])
    robots_txt = IntegerField('robots.txt', validators=[DataRequired(), NumberRange(min=1, max=10)])
    sitemap_xml = IntegerField('sitemap.xml', validators=[DataRequired(), NumberRange(min=1, max=10)])

    submit = SubmitField("Save")


class PageScoresForm(FlaskForm):

    h1_tags = IntegerField('H1 Tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    h2_tags = IntegerField('H2 Tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    h3_tags = IntegerField('H3 Tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    alt_tags = IntegerField('Alt Tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    meta_descriptions = IntegerField('Meta Descriptions', validators=[DataRequired(), NumberRange(min=1, max=10)])
    title_text = IntegerField('Title Text', validators=[DataRequired(), NumberRange(min=1, max=10)])
    view_state = IntegerField('View State', validators=[DataRequired(), NumberRange(min=1, max=10)])
    pagination = IntegerField('Pagination', validators=[DataRequired(), NumberRange(min=1, max=10)])
    iframe_content = IntegerField('Iframe Content', validators=[DataRequired(), NumberRange(min=1, max=10)])
    flash_attribute = IntegerField('Flash Attribute', validators=[DataRequired(), NumberRange(min=1, max=10)])
    no_index_no_follow_attribute = IntegerField('No Index No Follow Attribute', validators=[DataRequired(), NumberRange(min=1, max=10)])
    schema_tags = IntegerField('Schema Tags', validators=[DataRequired(), NumberRange(min=1, max=10)])
    blog_locations = IntegerField('Blog Locations', validators=[DataRequired(), NumberRange(min=1, max=10)])

    submit = SubmitField("Save")
