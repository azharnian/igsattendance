from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, PasswordField, SelectField, BooleanField, FieldList, FormField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CreateRoleForm(FlaskForm):
    rolecode = StringField('Role Code', validators=[DataRequired()])
    rolename = StringField('Role Name', validators=[DataRequired()])
    submit = SubmitField('Create')

class UpdateRoleForm(CreateRoleForm):
    submit = SubmitField('Update')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Ingat Saya')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Length(min=4)])
    # card = StringField('Student Card ID', validators=[DataRequired()])
    # nisn = StringField('NISN', validators=[DataRequired()])
    # nis = StringField('NIS', validators=[DataRequired()])
    # phone = StringField('Phone Number', validators=[DataRequired()])
    # gender = BooleanField('Gender', validators=[DataRequired()])
    # place = StringField('Place of Birth', validators=[DataRequired()])
    # birth = DateField('Date of Birth', validators=[DataRequired()])
    # origin = StringField('Origin', validators=[DataRequired()])
    # guardian = StringField('Guardian Name', validators=[DataRequired()])
    # contact = StringField('Guardian Contact', validators=[DataRequired()])
    # role = SelectField('Role', choices=[], validators=[DataRequired()])
    # image = FileField('Image', validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    submit = SubmitField('Register')

class UpdateUserForm(RegistrationForm):
    password, confirm_password = None, None
    active = BooleanField('Active')
    submit = SubmitField('Update')

class UpdatePasswordForm(FlaskForm):
    current = PasswordField('Current Password', validators=[DataRequired(), Length(min=4)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password'), Length(min=4)])
    submit = SubmitField('Update Password')

class RequestResetUserForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Request Reset Account')

class ResetUserForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password'), Length(min=4)])
    submit = SubmitField('Reset Password')

class CreateAuthTypeForm(FlaskForm):
    auth_type = StringField('Auth Type Name')
    submit = SubmitField('Create Auth Type')

class UpdateAuthTypeForm(CreateAuthTypeForm):
    active = BooleanField('Active')
    submit = SubmitField('Update Auth')

class CreateAuthMemberForm(FlaskForm):
    auth_type = SelectField('Auth Type')
    students = FieldList('Members', FormField(), min_entries=1)  
    submit = SubmitField('Register All')

class CreateDepartmentForm(FlaskForm):
    department_code = StringField('Department Code')
    department_name = StringField('Department Name')
    note = StringField('Note')
    submit = SubmitField('Create Department')

class UpdateDepartmentForm(CreateDepartmentForm):
    active = BooleanField('Active')
    submit = SubmitField('Update Department')

class CreateAcademicYear(FlaskForm):
    academic_year_code = StringField('Academic Year Code')
    academic_year_name = StringField('Academic Year Name')
    note = StringField('Note')
    submit = SubmitField('Create Academic Year')

class UpdateAcademicYear(CreateAcademicYear):
    active = BooleanField('Active')
    submit = SubmitField('Update Academic Year')

class CreateClassTypeForm(FlaskForm):
    class_code = StringField('Class Code')
    class_type = StringField('Class Type')
    academic_year = SelectField('Academic Year')
    submit = SubmitField('Create')

class UpdateClassTypeForm(CreateClassTypeForm):
    active = BooleanField('Active')
    submit = SubmitField('Update')

class CreateClassForm(FlaskForm):
    class_name = StringField('Class', validators=[DataRequired()])
    class_type = SelectField('Class Type')
    room = SelectField('Room')
    note = StringField('Note', validators=[DataRequired()])
    submit = SubmitField('Create')

class UpdateClassForm(CreateClassForm):
    active = BooleanField('Active')
    submit = SubmitField('Update')

class CreateClassMemberForm(FlaskForm):
    class_name = SelectField('Class Name')
    students = FieldList('Members', FormField(), min_entries=1)  
    submit = SubmitField('Register All')