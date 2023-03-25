from flask_wtf import Form, CSRFProtect
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class TypeForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    description = TextAreaField(
        'description'
    )
