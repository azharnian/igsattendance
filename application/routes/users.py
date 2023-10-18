from flask import Blueprint
from flask_login import login_required

from application.forms.users import *
from application.utils.users import *

users = Blueprint('users', __name__)

#SESSION
@users.route('/login', methods=['GET', 'POST'])
def login():
    pass

@users.route('/logout')
@login_required
def logout():
    pass


#USER_PAGE

#dasboard
@users.route('/')
@login_required
def index():
    pass

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