from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

from application.config import Config, DevConfig

db = SQLAlchemy()
redis = FlaskRedis()
migrate = Migrate()
mail = Mail()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_class=DevConfig):
    app = Flask(__name__, template_folder='views')
    app.config.from_object(DevConfig)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    redis.init_app(app)
    migrate.init_app(app, db)

    from application.routes.locations import locations
    from application.routes.users import users
    from application.routes.attendances import attendances
    from application.routes.logs import logs


    app.register_blueprint(locations)
    app.register_blueprint(users)
    app.register_blueprint(attendances)
    app.register_blueprint(logs)

    return app