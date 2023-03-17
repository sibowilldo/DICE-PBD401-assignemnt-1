from flask_wtf import Form, CSRFProtect
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email = EmailField(
        'email', validators=[DataRequired()]
    )
    password = PasswordField(
        'password', validators=[DataRequired()]
    )
