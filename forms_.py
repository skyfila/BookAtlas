from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired
from flask_login import UserMixin
from replit import db


db = db

class LoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField("password", validators=[DataRequired()])

class SignupForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField("password", validators=[DataRequired()])

