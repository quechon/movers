from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ReviewForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired(message='First name is required')])
    last_name = StringField('Last Name', validators=[DataRequired(message='Last name is required')])
    email = StringField('Email', validators=[DataRequired(message='Email is required')])
    message = TextAreaField('Message', validators=[DataRequired(message='Message required')])
