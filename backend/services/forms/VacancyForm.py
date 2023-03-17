from flask_wtf import Form, CSRFProtect
from wtforms import StringField, TextAreaField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, AnyOf, URL
from database.models import Type, Category


def category_choices():
    return map(lambda category: (category.id, category.name), Category.query.all())


def type_choices():

    return map(lambda type: (type.id, type.name), Type.query.all())


class VacancyForm(Form):
    user_id = HiddenField(
        'user_id', validators=[DataRequired()]
    )
    title = StringField(
        'title', validators=[DataRequired()]
    )
    description = TextAreaField(
        'description'
    )

    department = StringField(
        'department', validators=[DataRequired()]
    )


    location = SelectField(
        'location', validators=[DataRequired()],
        choices=['Steve Biko', 'Ritson', 'ML Sultan', 'Indumiso', 'Other']
    )


    expires_at = DateField(
        'expires_at', validators=[DataRequired()]
    )

    category_id = SelectField(
        'category_id', validators=[DataRequired()],
        choices=list(category_choices())
    )

    type_id = SelectField(
        'type_id', validators=[DataRequired()],
        choices=list(type_choices())
    )

