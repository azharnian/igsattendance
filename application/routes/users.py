from flask import render_template, redirect, url_for, request, flash
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
            next_url = request.args.get('next') or url_for('index')
            flash('Login Successful.', 'success')
            return redirect(next_url)
        flash('Sorry, Login Failed.', 'danger')
    return render_template('pages/login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


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

@users.route('/register', methods=['GET', 'POST'])
def register():
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