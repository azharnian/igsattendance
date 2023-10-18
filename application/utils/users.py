from application import db, login_manager
from application.models.users import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))