from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, PasswordField, SelectField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CreateReportLogForm(FlaskForm):
    pass
