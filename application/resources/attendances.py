from application import db
from application.models.attendances import *

##SHIFT

# Create a new Shift
def create_shift(data_json):
    data = data_json
    shift = Shift(
        note=data.get('note'),
        active=data.get('active', True),
        created_by=data.get('created_by', 0),
        shift_code=data['shift_code'],
        shift_name=data['shift_name'],
        start=data['start'],
        end=data['end']
    )
    db.session.add(shift)
    db.session.commit()
    return {"message": "Shift created successfully"}, 201

# Read all Shifts
def get_shifts():
    shifts = Shift.query.all()
    shift_list = []
    for shift in shifts:
        shift_data = {
            "id": shift.id,
            "note": shift.note,
            "active": shift.active,
            "create_date": shift.create_date,
            "created_by": shift.created_by,
            "shift_code": shift.shift_code,
            "shift_name": shift.shift_name,
            "start": shift.start,
            "end": shift.end
        }
        shift_list.append(shift_data)
    return {"shifts": shift_list}

# Read a specific Shift by ID
def get_shift(shift_id):
    shift = Shift.query.get(shift_id)
    if shift:
        shift_data = {
            "id": shift.id,
            "note": shift.note,
            "active": shift.active,
            "create_date": shift.create_date,
            "created_by": shift.created_by,
            "shift_code": shift.shift_code,
            "shift_name": shift.shift_name,
            "start": shift.start,
            "end": shift.end
        }
        return {"shift": shift_data}
    return {"message": "Shift not found"}, 404

# Update a Shift by ID
def update_shift(shift_id, new_shift_json):
    data = new_shift_json
    shift = Shift.query.get(shift_id)
    if shift:
        shift.note = data.get('note', shift.note)
        shift.active = data.get('active', shift.active)
        shift.created_by = data.get('created_by', shift.created_by)
        shift.shift_code = data.get('shift_code', shift.shift_code)
        shift.shift_name = data.get('shift_name', shift.shift_name)
        shift.start = data.get('start', shift.start)
        shift.end = data.get('end', shift.end)
        db.session.commit()
        return {"message": "Shift updated successfully"}
    return {"message": "Shift not found"}, 404

# Delete a Shift by ID
def delete_shift(shift_id):
    shift = Shift.query.get(shift_id)
    if shift:
        db.session.delete(shift)
        db.session.commit()
        return {"message": "Shift deleted successfully"}
    return {"message": "Shift not found"}, 404


##SHIFT MEMBER

# Create a new ShiftMember
def create_shift_member(data_json):
    data = data_json
    shift_member = ShiftMember(
        active=data.get('active', True),
        created_by=data.get('created_by', 0),
        user_id=data['user_id'],
        shift_id=data['shift_id']
    )
    db.session.add(shift_member)
    db.session.commit()
    return {"message": "ShiftMember created successfully"}, 201

# Read all ShiftMembers
def get_shift_members():
    shift_members = ShiftMember.query.all()
    shift_member_list = []
    for shift_member in shift_members:
        shift_member_data = {
            "id": shift_member.id,
            "active": shift_member.active,
            "create_date": shift_member.create_date,
            "created_by": shift_member.created_by,
            "user_id": shift_member.user_id,
            "shift_id": shift_member.shift_id
        }
        shift_member_list.append(shift_member_data)
    return {"shift_members": shift_member_list}

# Read a specific ShiftMember by ID
def get_shift_member(shift_member_id):
    shift_member = ShiftMember.query.get(shift_member_id)
    if shift_member:
        shift_member_data = {
            "id": shift_member.id,
            "active": shift_member.active,
            "create_date": shift_member.create_date,
            "created_by": shift_member.created_by,
            "user_id": shift_member.user_id,
            "shift_id": shift_member.shift_id
        }
        return {"shift_member": shift_member_data}
    return {"message": "ShiftMember not found"}, 404

# Update a ShiftMember by ID
def update_shift_member(shift_member_id, new_shift_member_json):
    data = new_shift_member_json
    shift_member = ShiftMember.query.get(shift_member_id)
    if shift_member:
        shift_member.active = data.get('active', shift_member.active)
        shift_member.created_by = data.get('created_by', shift_member.created_by)
        shift_member.user_id = data.get('user_id', shift_member.user_id)
        shift_member.shift_id = data.get('shift_id', shift_member.shift_id)
        db.session.commit()
        return {"message": "ShiftMember updated successfully"}
    return {"message": "ShiftMember not found"}, 404

# Delete a ShiftMember by ID
def delete_shift_member(shift_member_id):
    shift_member = ShiftMember.query.get(shift_member_id)
    if shift_member:
        db.session.delete(shift_member)
        db.session.commit()
        return {"message": "ShiftMember deleted successfully"}
    return {"message": "ShiftMember not found"}, 404

##STATUS

# Create a new Status
def create_status(data_json):
    data = data_json
    status = Status(
        note=data.get('note'),
        active=data.get('active', True),
        created_by=data.get('created_by', 0),
        status_code=data['status_code'],
        status_name=data['status_name']
    )
    db.session.add(status)
    db.session.commit()
    return {"message": "Status created successfully"}, 201

# Read all Statuses
def get_statuses():
    statuses = Status.query.all()
    status_list = []
    for status in statuses:
        status_data = {
            "id": status.id,
            "note": status.note,
            "active": status.active,
            "create_date": status.create_date,
            "created_by": status.created_by,
            "status_code": status.status_code,
            "status_name": status.status_name
        }
        status_list.append(status_data)
    return {"statuses": status_list}

# Read a specific Status by ID
def get_status(status_id):
    status = Status.query.get(status_id)
    if status:
        status_data = {
            "id": status.id,
            "note": status.note,
            "active": status.active,
            "create_date": status.create_date,
            "created_by": status.created_by,
            "status_code": status.status_code,
            "status_name": status.status_name
        }
        return {"status": status_data}
    return {"message": "Status not found"}, 404

# Update a Status by ID
def update_status(status_id, new_status_json):
    data = new_status_json
    status = Status.query.get(status_id)
    if status:
        status.note = data.get('note', status.note)
        status.active = data.get('active', status.active)
        status.created_by = data.get('created_by', status.created_by)
        status.status_code = data.get('status_code', status.status_code)
        status.status_name = data.get('status_name', status.status_name)
        db.session.commit()
        return {"message": "Status updated successfully"}
    return {"message": "Status not found"}, 404

# Delete a Status by ID
def delete_status(status_id):
    status = Status.query.get(status_id)
    if status:
        db.session.delete(status)
        db.session.commit()
        return {"message": "Status deleted successfully"}
    return {"message": "Status not found"}, 404

##ATTENDENCES

# Create a new Attendance
def create_attendance(data_json):
    data = data_json
    attendance = Attendance(
        note=data.get('note'),
        active=data.get('active', True),
        created_by=data.get('created_by', 0),
        user_id=data['user_id'],
        status_id=data['status_id'],
        room_id=data['room_id'],
        evidence_pic_url=data.get('evidence_pic_url')
    )
    db.session.add(attendance)
    db.session.commit()
    return {"message": "Attendance created successfully"}, 201

# Read all Attendances
def get_attendances():
    attendances = Attendance.query.all()
    attendance_list = []
    for attendance in attendances:
        attendance_data = {
            "id": attendance.id,
            "note": attendance.note,
            "active": attendance.active,
            "create_date": attendance.create_date,
            "created_by": attendance.created_by,
            "user_id": attendance.user_id,
            "status_id": attendance.status_id,
            "room_id": attendance.room_id,
            "evidence_pic_url": attendance.evidence_pic_url
        }
        attendance_list.append(attendance_data)
    return {"attendances": attendance_list}

# Read a specific Attendance by ID
def get_attendance(attendance_id):
    attendance = Attendance.query.get(attendance_id)
    if attendance:
        attendance_data = {
            "id": attendance.id,
            "note": attendance.note,
            "active": attendance.active,
            "create_date": attendance.create_date,
            "created_by": attendance.created_by,
            "user_id": attendance.user_id,
            "status_id": attendance.status_id,
            "room_id": attendance.room_id,
            "evidence_pic_url": attendance.evidence_pic_url
        }
        return {"attendance": attendance_data}
    return {"message": "Attendance not found"}, 404

# Update an Attendance by ID
def update_attendance(attendance_id, new_attendence_json):
    data = new_attendence_json
    attendance = Attendance.query.get(attendance_id)
    if attendance:
        attendance.note = data.get('note', attendance.note)
        attendance.active = data.get('active', attendance.active)
        attendance.created_by = data.get('created_by', attendance.created_by)
        attendance.user_id = data.get('user_id', attendance.user_id)
        attendance.status_id = data.get('status_id', attendance.status_id)
        attendance.room_id = data.get('room_id', attendance.room_id)
        attendance.evidence_pic_url = data.get('evidence_pic_url', attendance.evidence_pic_url)
        db.session.commit()
        return {"message": "Attendance updated successfully"}
    return {"message": "Attendance not found"}, 404

# Delete an Attendance by ID
def delete_attendance(attendance_id):
    attendance = Attendance.query.get(attendance_id)
    if attendance:
        db.session.delete(attendance)
        db.session.commit()
        return {"message": "Attendance deleted successfully"}
    return {"message": "Attendance not found"}, 404

