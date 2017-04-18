from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo

from app.users.models import User


class LoginForm(FlaskForm):

    email = StringField('Email Address', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Log in")


class RegistrationForm(FlaskForm):

    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    username = StringField("Username", validators=[Required(), Length(1, 64), Regexp("^[A-Za-z][A-Za-z0-9_.]*$",
                                                                                     0,
                                                                                     "Usernames must only have letters, \
                                                                                      numbers, dots or underscores.")])

    password = PasswordField("Password", validators=[Required(), EqualTo("password_two", message="Passwords must match.")])
    password_two = PasswordField("Confirm password", validators=[Required()])

    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")
