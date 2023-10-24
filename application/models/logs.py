from datetime import datetime

from application import db

class Event(db.Model):
    # create, read, update, delete, log in, log out, click
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    event_name = db.Column(db.String(256), uniqie=True, nullable=False)
    note = db.Column(db.String(256))

class Component(db.Model):
    # User, Location, Attendance, Log
    __tablename__ = "components"
    id = db.Column(db.Integer, primary_key=True)
    component_name = db.Column(db.String(256), unique=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    note = db.Column(db.String(256))

class Log(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    affected_user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("activities.id", nullable=False))
    ip_address = db.Column(db.String(256), nullable=False)
    