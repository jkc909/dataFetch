from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AddUrlToQueue(FlaskForm):
	url = StringField('Enter the URL:')
	submit = SubmitField('Submit URL')

class ViewData(FlaskForm):
	url = StringField('Enter the URL:')
	submit = SubmitField('Submit URL')