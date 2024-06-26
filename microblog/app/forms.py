from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# This is a login form
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')