from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, PasswordField, SelectField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CreateAttendanceForm(FlaskForm):
    methods = SelectField('Method')
    card_number = StringField('Your ID Number')
    submit = SubmitField('Enter')

class CreateManualAttendanceForm(FlaskForm):
    student_number = StringField('Student Number')
    status = SelectField('Status')
    evidence = FileField('Evidence')
    note = StringField('Note')
    submit = SubmitField('Enter')

class UpdateAttendanceForm(FlaskForm):
    pass

class MakeConfirmationUpdateForm(FlaskForm):
    pass

class CreateReportAttendance(FlaskForm):
    pass
