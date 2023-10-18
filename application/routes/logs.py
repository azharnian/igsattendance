from flask import Blueprint
from flask_login import login_required

from application.forms.logs import *
from application.utils.logs import *

logs = Blueprint('logs', __name__)