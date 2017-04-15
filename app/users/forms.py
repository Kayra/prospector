from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(FlaskForm):

    email = StringField('url', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Log in")
