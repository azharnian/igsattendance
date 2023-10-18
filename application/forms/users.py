from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, PasswordField, SelectField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    card = StringField('Student Card ID', validators=[DataRequired()])
    nisn = StringField('NISN', validators=[DataRequired()])
    nis = StringField('NIS', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    gender = BooleanField('Gender', validators=[DataRequired()])
    place = StringField('Place of Birth', validators=[DataRequired()])
    birth = DateField('Date of Birth', validators=[DataRequired()])
    origin = StringField('Origin', validators=[DataRequired()])
    guardian = StringField('Guardian Name', validators=[DataRequired()])
    contact = StringField('Guardian Contact', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Length(min=4)])
    role = SelectField('Role', choices=[], validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    active = BooleanField('Active')
    submit = SubmitField('Register')

class UpdateUserForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    card = StringField('Student Card ID', validators=[DataRequired()])
    nisn = StringField('NISN', validators=[DataRequired()])
    nis = StringField('NIS', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    gender = BooleanField('Gender', validators=[DataRequired()])
    place = StringField('Place of Birth', validators=[DataRequired()])
    birth = DateField('Date of Birth', validators=[DataRequired()])
    origin = StringField('Origin', validators=[DataRequired()])
    guardian = StringField('Guardian Name', validators=[DataRequired()])
    contact = StringField('Guardian Contact', validators=[DataRequired()])
    role = SelectField('Role', choices=[], validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    active = BooleanField('Active')
    submit = SubmitField('Update')

class UpdatePasswordForm(FlaskForm):
    current = PasswordField('Current Password', validators=[DataRequired(), Length(min=4)])
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password'), Length(min=4)])
    submit = SubmitField('Update Password')

class RequestResetUserForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    nisn = StringField('NISN', validators=[DataRequired()])
    submit = SubmitField('Request Reset Account')

class ResetUserForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password'), Length(min=4)])
    submit = SubmitField('Reset Password')

class CreateCohortForm(FlaskForm):
    cohort = StringField('Cohort', validators=[DataRequired()])
    active = BooleanField('Active')
    note = StringField('Note', validators=[DataRequired()])
    submit = SubmitField('Create Cohort')

class CreateAcademicYearForm(FlaskForm):
    year = StringField('Year Academic', validators=[DataRequired()])
    active = BooleanField('Active')
    note = StringField('Note', validators=[DataRequired()])
    submit = SubmitField('Create Year')

class CreateRoleForm(FlaskForm):
    role = StringField('Role', validators=[DataRequired()])
    active = BooleanField('Active')
    note = StringField('Note', validators=[DataRequired()])
    submit = SubmitField('Create Role')


class CreateOrganizationForm(FlaskForm):
    organization = StringField('Organization', validators=[DataRequired()])
    active = BooleanField('Active')
    note = StringField('Note', validators=[DataRequired()])
    submit = SubmitField('Create Role')