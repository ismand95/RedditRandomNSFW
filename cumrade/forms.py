from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class GenerateRandom(FlaskForm):
    #username = StringField('Brugernavn', validators=[DataRequired()])
    submit = SubmitField('Random NSFW')
