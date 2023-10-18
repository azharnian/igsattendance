from flask_login import UserMixin

from application import db

class Organization(db.Model):
    pass

class Role(db.Model):
    pass

class Cohort(db.Model):
    pass

class User(db.Model, UserMixin):
    pass
