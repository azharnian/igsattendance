from application.models.users import *

def get_user_by_username(username):
    return User.query.filter_by(username = username).first()