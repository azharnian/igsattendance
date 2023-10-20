from datetime import datetime

from application import db

class Shift(db.Model):
    __tablename__ = 'shifts'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    shift_code = db.Column(db.String(256), unique=True, nullable=False)
    shift_name = db.Column(db.String(256), nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)

class ShiftMember(db.Model):
    __tablename__ = 'shift_members'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    shift_id = db.Column(db.Integer, db.ForeignKey("shifts.id"), nullable=False)

class Status(db.Model):
    #masuk , izin, sakit, dispensasi
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    status_code = db.Column(db.String(256), unique=True, nullable=False)
    status_name = db.Column(db.String(256), nullable=False)

class Attendance(db.Model):
    __attendance__ = 'attendances'
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    active = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"), nullable=False, default=0)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable=False)
    evidence_pic_url = db.Column(db.String(256))