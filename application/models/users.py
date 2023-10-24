from flask_login import UserMixin

from datetime import datetime

from application import db
from application.models.locations import Room

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    role_code = db.Column(db.String(256), unique=True, nullable=False)
    role_name = db.Column(db.String(256), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
class User(db.Model, UserMixin): 
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(256), nullable=False)
    username = db.Column(db.String(256), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False, default=0)
    # created_date = db.Column(db.DateTime, default=datetime.utcnow)

class AuthType(db.Model):
    # barcode, nfc, face, etc
    __tablename__ = "auth_types"
    id = db.Column(db.Integer, primary_key=True)
    auth_type_name = db.Column(db.String(256), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, default=0)

class AuthMember(db.Model):
    __tablename__ = "auths"
    id = db.Column(db.Integer, primary_key=True)
    auth_type_id = db.Column(db.Integer, db.ForeignKey("auth_types.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    active = db.Column(db.Boolean, default=True)
    register_date = db.Column(db.DateTime, default=datetime.utcnow)
    registered_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, default=0)

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    status = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    department_code = db.Column(db.String(256), unique=True, nullable=False)
    department_name = db.Column(db.String(256), nullable=False)

class DepartmentMember(db.Model):
    __tablename__ = "department_members"
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    active = db.Column(db.Boolean, default=True)
    enroll_date = db.Column(db.DateTime, default=datetime.utcnow)
    enrolled_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, default=0)

class AcademicYear(db.Model):
    __tablename__ = "academic_years"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))
    status = db.Column(db.Boolean, nullable=False, default=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), default=0)
    academic_year_code = db.Column(db.String(256), unique=True, nullable=False)
    academic_year_name = db.Column(db.String(256), nullable=False)

class ClassType(db.Model):
    __tablename__ ="class_types"
    #regular, mulok, ekskul
    id = db.Column(db.Integer, primary_key=True)
    class_code = db.Column(db.String(256), unique=True, nullable=False)
    class_type = db.Column(db.String(256), unique=True, nullable=False)
    academic_year_id = db.Column(db.Integer, db.ForeignKey("academic_years.id"), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, default=0)

class Class(db.Model):
    __tablename__ = "classes"
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(256), nullable=False)
    class_type = db.Column(db.Integer, db.ForeignKey("class_types.id"), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, default=0)

class ClassMember(db.Model):
    __tablename__ = "class_members"
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    active = db.Column(db.Boolean, default=True)
    enroll_date = db.Column(db.DateTime, default=datetime.utcnow)
    enrolled_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, default=0)