import os
from decouple import config as cf
from dotenv import load_dotenv

load_dotenv()

class Config:
    PYTHONDONTWRITEBYTECODE = cf('PYTHONDONTWRITEBYTECODE', default=False, cast=bool)

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_TM')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_ADDRESS')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')