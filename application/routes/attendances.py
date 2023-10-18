from flask import Blueprint
from flask_login import login_required

from application.forms.attendances import *
from application.utils.attendances import *

attendances = Blueprint('attendances', __name__)

#ENTRY
@attendances.route('/entry', methods=['GET', 'POST'])
@login_required
def entry():
    pass

@attendances.route('/manual', methods=['GET', 'POST'])
@login_required
def manual():
    pass

@attendances.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    pass


#REPORT
@attendances.route('/report')
@login_required
def report():
    pass
