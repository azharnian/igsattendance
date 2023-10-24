from flask import render_template, redirect, url_for, jsonify, flash, request
from flask import Blueprint
from flask_login import login_required, login_user, logout_user

from application.forms.users import *
from application.utils.users import *
from application.resources.users import *

users = Blueprint('users', __name__)

#SESSION
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = get_user_login(form.username.data)
        user = data['user']
        if user and user.password == form.password.data:
            login_user(user)
            next_url = request.args.get('next') or url_for('users.index')
            flash('Login Successful.', 'success')
            return redirect(next_url)
        flash('Sorry, Login Failed.', 'danger')
    return render_template('pages/login.html', title='Login', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Get form data
        fullname = form.fullname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        data_json = jsonify({
            'fullname': fullname,
            'username': username,
            'email': email,
            'password': password
        })

        response = create_user(data_json)
        flash(response.get_json()['message'], 'success')
        if response.status_code == 201:
            return redirect(url_for('users.login'))

    return render_template('pages/register.html', title='Registration', form=form)


#USER_PAGE

#dasboard
@users.route('/')
@login_required
def index():
    return render_template("index.html")

@users.route('/profile')
@login_required
def profile():
    pass

@users.route('/forgot', methods=['GET', 'POST'])
def forgot():
    pass

@users.route('/reset', methods=['GET', 'POST'])
@login_required
def reset():
    pass


#ADMIN_PAGE
@users.route('/logs', methods=['GET', 'POST'])
@login_required
def logs():
    pass

@users.route('/confirm', methods=['GET', 'POST'])
@login_required
def confirm():
    pass

@users.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    pass

@users.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    pass

@users.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    pass