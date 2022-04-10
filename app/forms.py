# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField,TextAreaField,DecimalField,IntegerField,SelectField
from wtforms.validators import InputRequired


class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired()])
    photo =FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png','jpeg'], 'Images only!')])
