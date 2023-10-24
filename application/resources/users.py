from flask import jsonify, make_response
from application.models.users import *

##ROLE

# Create a new Role
def create_role(data_json):
    data = data_json
    role = Role(
        role_code=data['role_code'],
        role_name=data['role_name'],
        active=data.get('active', True)
    )
    db.session.add(role)
    db.session.commit()
    return {"message": "Role created successfully"}, 201

# Read all Roles
def get_roles():
    roles = Role.query.all()
    role_list = []
    for role in roles:
        role_data = {
            "id": role.id,
            "role_code": role.role_code,
            "role_name": role.role_name,
            "active": role.active,
            "created_date": role.created_date
        }
        role_list.append(role_data)
    return {"roles": role_list}

# Read a specific Role by ID
def get_role(role_id):
    role = Role.query.get(role_id)
    if role:
        role_data = {
            "id": role.id,
            "role_code": role.role_code,
            "role_name": role.role_name,
            "active": role.active,
            "created_date": role.created_date
        }
        return {"role": role_data}
    return {"message": "Role not found"}, 404

# Update a Role by ID
def update_role(role_id, new_role_json):
    data = new_role_json
    role = Role.query.get(role_id)
    if role:
        role.role_code = data.get('role_code', role.role_code)
        role.role_name = data.get('role_name', role.role_name)
        role.active = data.get('active', role.active)
        db.session.commit()
        return {"message": "Role updated successfully"}
    return {"message": "Role not found"}, 404

# Delete a Role by ID
def delete_role(role_id):
    role = Role.query.get(role_id)
    if role:
        db.session.delete(role)
        db.session.commit()
        return {"message": "Role deleted successfully"}
    return {"message": "Role not found"}, 404


##USER

# Create a new User
def create_user(data_json):
    data = data_json.json
    user = User(
        fullname=data['fullname'],
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role_id=data.get('role_id', 0)
    )
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify({"message": "User created successfully"}), 201)

# Read all Users
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            "id": user.id,
            "fullname": user.fullname,
            "username": user.username,
            "email": user.email,
            "role_id": user.role_id
        }
        user_list.append(user_data)
    return {"users": user_list}

# Read a specific User by ID
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            "id": user.id,
            "fullname": user.fullname,
            "username": user.username,
            "email": user.email,
            "role_id": user.role_id
        }
        return {"user": user_data}
    return {"message": "User not found"}, 404

# Read a specific User for Login by Username using User Object
def get_user_login(username):
    user = User.query.filter_by(username = username).first()
    if user:
        return {"user": user}
    return {"message": "User not found"}, 404

# Update a User by ID
def update_user(user_id, new_user_json):
    data = new_user_json
    user = User.query.get(user_id)
    if user:
        user.fullname = data.get('fullname', user.fullname)
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        user.role_id = data.get('role_id', user.role_id)
        db.session.commit()
        return {"message": "User updated successfully"}
    return {"message": "User not found"}, 404

# Delete a User by ID
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}
    return {"message": "User not found"}, 404

##AUTHTYPE

# Create a new AuthType
def create_auth_type(data_json):
    data = data_json
    auth_type = AuthType(
        auth_type_name=data['auth_type_name'],
        active=data.get('active', True)
    )
    db.session.add(auth_type)
    db.session.commit()
    return {"message": "AuthType created successfully"}, 201

# Read all AuthTypes
def get_auth_types():
    auth_types = AuthType.query.all()
    auth_type_list = []
    for auth_type in auth_types:
        auth_type_data = {
            "id": auth_type.id,
            "auth_type_name": auth_type.auth_type_name,
            "active": auth_type.active,
            "created_date": auth_type.created_date
        }
        auth_type_list.append(auth_type_data)
    return {"auth_types": auth_type_list}

# Read a specific AuthType by ID
def get_auth_type(auth_type_id):
    auth_type = AuthType.query.get(auth_type_id)
    if auth_type:
        auth_type_data = {
            "id": auth_type.id,
            "auth_type_name": auth_type.auth_type_name,
            "active": auth_type.active,
            "created_date": auth_type.created_date
        }
        return {"auth_type": auth_type_data}
    return {"message": "AuthType not found"}, 404

# Update an AuthType by ID
def update_auth_type(auth_type_id, new_auth_type_json):
    data = new_auth_type_json
    auth_type = AuthType.query.get(auth_type_id)
    if auth_type:
        auth_type.auth_type_name = data.get('auth_type_name', auth_type.auth_type_name)
        auth_type.active = data.get('active', auth_type.active)
        db.session.commit()
        return {"message": "AuthType updated successfully"}
    return {"message": "AuthType not found"}, 404

# Delete an AuthType by ID
def delete_auth_type(auth_type_id):
    auth_type = AuthType.query.get(auth_type_id)
    if auth_type:
        db.session.delete(auth_type)
        db.session.commit()
        return {"message": "AuthType deleted successfully"}
    return {"message": "AuthType not found"}, 404


##AUTH MEMBER

# Create a new AuthMember
def create_auth_member(data_json):
    data = data_json
    auth_member = AuthMember(
        auth_type_id=data['auth_type_id'],
        user_id=data['user_id'],
        active=data.get('active', True)
    )
    db.session.add(auth_member)
    db.session.commit()
    return {"message": "AuthMember created successfully"}, 201

# Read all AuthMembers
def get_auth_members():
    auth_members = AuthMember.query.all()
    auth_member_list = []
    for auth_member in auth_members:
        auth_member_data = {
            "id": auth_member.id,
            "auth_type_id": auth_member.auth_type_id,
            "user_id": auth_member.user_id,
            "active": auth_member.active,
            "register_date": auth_member.register_date,
            "registered_by": auth_member.registered_by
        }
        auth_member_list.append(auth_member_data)
    return {"auth_members": auth_member_list}

# Read a specific AuthMember by ID
def get_auth_member(auth_member_id):
    auth_member = AuthMember.query.get(auth_member_id)
    if auth_member:
        auth_member_data = {
            "id": auth_member.id,
            "auth_type_id": auth_member.auth_type_id,
            "user_id": auth_member.user_id,
            "active": auth_member.active,
            "register_date": auth_member.register_date,
            "registered_by": auth_member.registered_by
        }
        return {"auth_member": auth_member_data}
    return {"message": "AuthMember not found"}, 404

# Update an AuthMember by ID
def update_auth_member(auth_member_id, new_auth_member_json):
    data = new_auth_member_json
    auth_member = AuthMember.query.get(auth_member_id)
    if auth_member:
        auth_member.auth_type_id = data.get('auth_type_id', auth_member.auth_type_id)
        auth_member.user_id = data.get('user_id', auth_member.user_id)
        auth_member.active = data.get('active', auth_member.active)
        db.session.commit()
        return {"message": "AuthMember updated successfully"}
    return {"message": "AuthMember not found"}, 404

# Delete an AuthMember by ID
def delete_auth_member(auth_member_id):
    auth_member = AuthMember.query.get(auth_member_id)
    if auth_member:
        db.session.delete(auth_member)
        db.session.commit()
        return {"message": "AuthMember deleted successfully"}
    return {"message": "AuthMember not found"}, 404

##DEPARTMENT

# Create a new Department
def create_department(data_json):
    data = data_json
    department = Department(
        department_code=data['department_code'],
        department_name=data['department_name'],
        status=data.get('status', True),
        note=data.get('note', None),
        created_by=data.get('created_by', 0)
    )
    db.session.add(department)
    db.session.commit()
    return {"message": "Department created successfully"}, 201

# Read all Departments
def get_departments():
    departments = Department.query.all()
    department_list = []
    for department in departments:
        department_data = {
            "id": department.id,
            "department_code": department.department_code,
            "department_name": department.department_name,
            "status": department.status,
            "create_date": department.create_date,
            "created_by": department.created_by,
            "note": department.note
        }
        department_list.append(department_data)
    return {"departments": department_list}

# Read a specific Department by ID
def get_department(department_id):
    department = Department.query.get(department_id)
    if department:
        department_data = {
            "id": department.id,
            "department_code": department.department_code,
            "department_name": department.department_name,
            "status": department.status,
            "create_date": department.create_date,
            "created_by": department.created_by,
            "note": department.note
        }
        return {"department": department_data}
    return {"message": "Department not found"}, 404

# Update a Department by ID
def update_department(department_id, new_department_json):
    data = new_department_json
    department = Department.query.get(department_id)
    if department:
        department.department_code = data.get('department_code', department.department_code)
        department.department_name = data.get('department_name', department.department_name)
        department.status = data.get('status', department.status)
        department.note = data.get('note', department.note)
        department.created_by = data.get('created_by', department.created_by)
        db.session.commit()
        return {"message": "Department updated successfully"}
    return {"message": "Department not found"}, 404

# Delete a Department by ID
def delete_department(department_id):
    department = Department.query.get(department_id)
    if department:
        db.session.delete(department)
        db.session.commit()
        return {"message": "Department deleted successfully"}
    return {"message": "Department not found"}, 404


##DEPARTMENT MEMBER

# Create a new DepartmentMember
def create_department_member(data_json):
    data = data_json
    department_member = DepartmentMember(
        department_id=data['department_id'],
        user_id=data['user_id'],
        active=data.get('active', True),
        enroll_date=data.get('enroll_date', datetime.utcnow()),
        enrolled_by=data.get('enrolled_by', 0)
    )
    db.session.add(department_member)
    db.session.commit()
    return {"message": "DepartmentMember created successfully"}, 201

# Read all DepartmentMembers
def get_department_members():
    department_members = DepartmentMember.query.all()
    department_member_list = []
    for department_member in department_members:
        department_member_data = {
            "id": department_member.id,
            "department_id": department_member.department_id,
            "user_id": department_member.user_id,
            "active": department_member.active,
            "enroll_date": department_member.enroll_date,
            "enrolled_by": department_member.enrolled_by
        }
        department_member_list.append(department_member_data)
    return {"department_members": department_member_list}

# Read a specific DepartmentMember by ID
def get_department_member(department_member_id):
    department_member = DepartmentMember.query.get(department_member_id)
    if department_member:
        department_member_data = {
            "id": department_member.id,
            "department_id": department_member.department_id,
            "user_id": department_member.user_id,
            "active": department_member.active,
            "enroll_date": department_member.enroll_date,
            "enrolled_by": department_member.enrolled_by
        }
        return {"department_member": department_member_data}
    return {"message": "DepartmentMember not found"}, 404

# Update a DepartmentMember by ID
def update_department_member(department_member_id, new_department_member_json):
    data = new_department_member_json
    department_member = DepartmentMember.query.get(department_member_id)
    if department_member:
        department_member.department_id = data.get('department_id', department_member.department_id)
        department_member.user_id = data.get('user_id', department_member.user_id)
        department_member.active = data.get('active', department_member.active)
        department_member.enroll_date = data.get('enroll_date', department_member.enroll_date)
        department_member.enrolled_by = data.get('enrolled_by', department_member.enrolled_by)
        db.session.commit()
        return {"message": "DepartmentMember updated successfully"}
    return {"message": "DepartmentMember not found"}, 404

# Delete a DepartmentMember by ID
def delete_department_member(department_member_id):
    department_member = DepartmentMember.query.get(department_member_id)
    if department_member:
        db.session.delete(department_member)
        db.session.commit()
        return {"message": "DepartmentMember deleted successfully"}
    return {"message": "DepartmentMember not found"}, 404

##ACADEMIC YEAR

# Create a new AcademicYear
def create_academic_year(data_json):
    data = data_json
    academic_year = AcademicYear(
        academic_year_code=data['academic_year_code'],
        academic_year_name=data['academic_year_name'],
        status=data.get('status', True),
        note=data.get('note', None),
        created_by=data.get('created_by', 0)
    )
    db.session.add(academic_year)
    db.session.commit()
    return {"message": "AcademicYear created successfully"}, 201

# Read all AcademicYears
def get_academic_years():
    academic_years = AcademicYear.query.all()
    academic_year_list = []
    for academic_year in academic_years:
        academic_year_data = {
            "id": academic_year.id,
            "academic_year_code": academic_year.academic_year_code,
            "academic_year_name": academic_year.academic_year_name,
            "status": academic_year.status,
            "create_date": academic_year.create_date,
            "created_by": academic_year.created_by,
            "note": academic_year.note
        }
        academic_year_list.append(academic_year_data)
    return {"academic_years": academic_year_list}

# Read a specific AcademicYear by ID
def get_academic_year(academic_year_id):
    academic_year = AcademicYear.query.get(academic_year_id)
    if academic_year:
        academic_year_data = {
            "id": academic_year.id,
            "academic_year_code": academic_year.academic_year_code,
            "academic_year_name": academic_year.academic_year_name,
            "status": academic_year.status,
            "create_date": academic_year.create_date,
            "created_by": academic_year.created_by,
            "note": academic_year.note
        }
        return {"academic_year": academic_year_data}
    return {"message": "AcademicYear not found"}, 404

# Update an AcademicYear by ID
def update_academic_year(academic_year_id, new_academic_year_json):
    data = new_academic_year_json
    academic_year = AcademicYear.query.get(academic_year_id)
    if academic_year:
        academic_year.academic_year_code = data.get('academic_year_code', academic_year.academic_year_code)
        academic_year.academic_year_name = data.get('academic_year_name', academic_year.academic_year_name)
        academic_year.status = data.get('status', academic_year.status)
        academic_year.note = data.get('note', academic_year.note)
        academic_year.created_by = data.get('created_by', academic_year.created_by)
        db.session.commit()
        return {"message": "AcademicYear updated successfully"}
    return {"message": "AcademicYear not found"}, 404

# Delete an AcademicYear by ID
def delete_academic_year(academic_year_id):
    academic_year = AcademicYear.query.get(academic_year_id)
    if academic_year:
        db.session.delete(academic_year)
        db.session.commit()
        return {"message": "AcademicYear deleted successfully"}
    return {"message": "AcademicYear not found"}, 404


##CLASS TYPE

# Create a new ClassType
def create_class_type(data_json):
    data = data_json
    class_type = ClassType(
        class_code=data['class_code'],
        class_type=data['class_type'],
        academic_year_id=data['academic_year_id'],
        active=data.get('active', True),
        created_by=data.get('created_by', 0)
    )
    db.session.add(class_type)
    db.session.commit()
    return {"message": "ClassType created successfully"}, 201

# Read all ClassTypes
def get_class_types():
    class_types = ClassType.query.all()
    class_type_list = []
    for class_type in class_types:
        class_type_data = {
            "id": class_type.id,
            "class_code": class_type.class_code,
            "class_type": class_type.class_type,
            "academic_year_id": class_type.academic_year_id,
            "active": class_type.active,
            "created_date": class_type.created_date,
            "created_by": class_type.created_by
        }
        class_type_list.append(class_type_data)
    return {"class_types": class_type_list}

# Read a specific ClassType by ID
def get_class_type(class_type_id):
    class_type = ClassType.query.get(class_type_id)
    if class_type:
        class_type_data = {
            "id": class_type.id,
            "class_code": class_type.class_code,
            "class_type": class_type.class_type,
            "academic_year_id": class_type.academic_year_id,
            "active": class_type.active,
            "created_date": class_type.created_date,
            "created_by": class_type.created_by
        }
        return {"class_type": class_type_data}
    return {"message": "ClassType not found"}, 404

# Update a ClassType by ID
def update_class_type(class_type_id, new_class_type_json):
    data = new_class_type_json
    class_type = ClassType.query.get(class_type_id)
    if class_type:
        class_type.class_code = data.get('class_code', class_type.class_code)
        class_type.class_type = data.get('class_type', class_type.class_type)
        class_type.academic_year_id = data.get('academic_year_id', class_type.academic_year_id)
        class_type.active = data.get('active', class_type.active)
        class_type.created_by = data.get('created_by', class_type.created_by)
        db.session.commit()
        return {"message": "ClassType updated successfully"}
    return {"message": "ClassType not found"}, 404

# Delete a ClassType by ID
def delete_class_type(class_type_id):
    class_type = ClassType.query.get(class_type_id)
    if class_type:
        db.session.delete(class_type)
        db.session.commit()
        return {"message": "ClassType deleted successfully"}
    return {"message": "ClassType not found"}, 404


##CLASS

# Create a new Class
def create_class(data_json):
    data = data_json
    class_ = Class(
        class_name=data['class_name'],
        class_type=data['class_type'],
        room_id=data['room_id'],
        active=data.get('active', True),
        created_by=data.get('created_by', 0)
    )
    db.session.add(class_)
    db.session.commit()
    return {"message": "Class created successfully"}, 201

# Read all Classes
def get_classes():
    classes = Class.query.all()
    class_list = []
    for class_ in classes:
        class_data = {
            "id": class_.id,
            "class_name": class_.class_name,
            "class_type": class_.class_type,
            "room_id": class_.room_id,
            "active": class_.active,
            "created_date": class_.created_date,
            "created_by": class_.created_by
        }
        class_list.append(class_data)
    return {"classes": class_list}

# Read a specific Class by ID
def get_class(class_id):
    class_ = Class.query.get(class_id)
    if class_:
        class_data = {
            "id": class_.id,
            "class_name": class_.class_name,
            "class_type": class_.class_type,
            "room_id": class_.room_id,
            "active": class_.active,
            "created_date": class_.created_date,
            "created_by": class_.created_by
        }
        return {"class": class_data}
    return {"message": "Class not found"}, 404

# Update a Class by ID
def update_class(class_id, new_class_json):
    data = new_class_json
    class_ = Class.query.get(class_id)
    if class_:
        class_.class_name = data.get('class_name', class_.class_name)
        class_.class_type = data.get('class_type', class_.class_type)
        class_.room_id = data.get('room_id', class_.room_id)
        class_.active = data.get('active', class_.active)
        class_.created_by = data.get('created_by', class_.created_by)
        db.session.commit()
        return {"message": "Class updated successfully"}
    return {"message": "Class not found"}, 404

# Delete a Class by ID
def delete_class(class_id):
    class_ = Class.query.get(class_id)
    if class_:
        db.session.delete(class_)
        db.session.commit()
        return {"message": "Class deleted successfully"}
    return {"message": "Class not found"}, 404

##CLASSMEMBER

# Create a new ClassMember
def create_class_member(data_json):
    data = data_json
    class_member = ClassMember(
        class_id=data['class_id'],
        user_id=data['user_id'],
        active=data.get('active', True),
        enroll_date=data.get('enroll_date', datetime.utcnow()),
        enrolled_by=data.get('enrolled_by', 0)
    )
    db.session.add(class_member)
    db.session.commit()
    return {"message": "ClassMember created successfully"}, 201

# Read all ClassMembers
def get_class_members():
    class_members = ClassMember.query.all()
    class_member_list = []
    for class_member in class_members:
        class_member_data = {
            "id": class_member.id,
            "class_id": class_member.class_id,
            "user_id": class_member.user_id,
            "active": class_member.active,
            "enroll_date": class_member.enroll_date,
            "enrolled_by": class_member.enrolled_by
        }
        class_member_list.append(class_member_data)
    return {"class_members": class_member_list}

# Read a specific ClassMember by ID
def get_class_member(class_member_id):
    class_member = ClassMember.query.get(class_member_id)
    if class_member:
        class_member_data = {
            "id": class_member.id,
            "class_id": class_member.class_id,
            "user_id": class_member.user_id,
            "active": class_member.active,
            "enroll_date": class_member.enroll_date,
            "enrolled_by": class_member.enrolled_by
        }
        return {"class_member": class_member_data}
    return {"message": "ClassMember not found"}, 404

# Update a ClassMember by ID
def update_class_member(class_member_id, new_class_member_json):
    data = new_class_member_json
    class_member = ClassMember.query.get(class_member_id)
    if class_member:
        class_member.class_id = data.get('class_id', class_member.class_id)
        class_member.user_id = data.get('user_id', class_member.user_id)
        class_member.active = data.get('active', class_member.active)
        class_member.enroll_date = data.get('enroll_date', class_member.enroll_date)
        class_member.enrolled_by = data.get('enrolled_by', class_member.enrolled_by)
        db.session.commit()
        return {"message": "ClassMember updated successfully"}
    return {"message": "ClassMember not found"}, 404

# Delete a ClassMember by ID
def delete_class_member(class_member_id):
    class_member = ClassMember.query.get(class_member_id)
    if class_member:
        db.session.delete(class_member)
        db.session.commit()
        return {"message": "ClassMember deleted successfully"}
    return {"message": "ClassMember not found"}, 404
