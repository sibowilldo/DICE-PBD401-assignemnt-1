from flask_wtf import Form, CSRFProtect
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class StatusForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    description = TextAreaField(
        'description'
    )

    model_type = SelectField(
        'model_type', validators=[DataRequired()],
        choices=['applications', 'users'])

    priority = SelectField(
        'priority', validators=[DataRequired()],
        choices=range(10))

