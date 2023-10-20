from datetime import datetime

from application import db

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    location_code = db.Column(db.String(256), unique=True, nullable=False)
    location_name = db.Column(db.String(256), nullable=False)

class Building(db.Model):
    __tablename__ = "buildings"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    building_code = db.Column(db.String(256), unique=True, nullable=False)
    building_name = db.Column(db.String(256), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False, default=0)

class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    room_code = db.Column(db.String(256), unique=True, nullable=False)
    room_name = db.Column(db.String(256), nullable=False)
    builing_id = db.Column(db.Integer, db.ForeignKey("buildings.id"), nullable=False, default=0)