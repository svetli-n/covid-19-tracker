from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, RadioField, TextAreaField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, NumberRange, DataRequired, Length


class StateForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    status = RadioField('Status', choices=[('healthy', 'healthy'), ('infected', 'infected'), ('unsure', 'unsure')])
    symptoms = TextAreaField('Symptoms')
    age = IntegerField('Age', validators=[NumberRange(min=0, max=120)])
    gender = RadioField('Gender', choices=[('male', 'male'), ('female', 'female'), ('unspecified', 'unspecified')])
    zip_code = StringField('Zip code', validators=[DataRequired()])
    country_code = StringField('Country code', validators=[DataRequired(), Length(min=2, max=2)], default='se')
    submit = SubmitField('Submit')
