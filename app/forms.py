from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required

class UrlEntry(Form):
	url = StringField('url', validators = [Required()])