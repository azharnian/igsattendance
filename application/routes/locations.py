from flask import Blueprint
from flask_login import login_required

from application.forms.locations import *
from application.utils.locations import *

locations = Blueprint('locations', __name__)