from flask_wtf import Form, CSRFProtect
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, AnyOf, URL
from ...database.models import User


class RegisterForm(Form):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    given_name = StringField('given_name', validators=[DataRequired()])
    family_name = StringField('family_name', validators=[DataRequired()])
