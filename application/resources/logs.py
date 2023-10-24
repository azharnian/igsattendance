from application import db
from application.models.logs import *

##EVENT

# Create a new Event
def create_event(data_json):
    data = data_json
    event = Event(
        event_name=data['event_name'],
        note=data.get('note', None),
        created_by=data.get('created_by', 0)
    )
    db.session.add(event)
    db.session.commit()
    return {"message": "Event created successfully"}, 201

# Read all Events
def get_events():
    events = Event.query.all()
    event_list = []
    for event in events:
        event_data = {
            "id": event.id,
            "event_name": event.event_name,
            "create_date": event.create_date,
            "created_by": event.created_by,
            "note": event.note
        }
        event_list.append(event_data)
    return {"events": event_list}

# Read a specific Event by ID
def get_event(event_id):
    event = Event.query.get(event_id)
    if event:
        event_data = {
            "id": event.id,
            "event_name": event.event_name,
            "create_date": event.create_date,
            "created_by": event.created_by,
            "note": event.note
        }
        return {"event": event_data}
    return {"message": "Event not found"}, 404

# Update an Event by ID
def update_event(event_id, new_event_json):
    data = new_event_json
    event = Event.query.get(event_id)
    if event:
        event.event_name = data.get('event_name', event.event_name)
        event.note = data.get('note', event.note)
        event.created_by = data.get('created_by', event.created_by)
        db.session.commit()
        return {"message": "Event updated successfully"}
    return {"message": "Event not found"}, 404

# Delete an Event by ID
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return {"message": "Event deleted successfully"}
    return {"message": "Event not found"}, 404

##COMPONENT

# Create a new Component
def create_component(data_json):
    data = data_json
    component = Component(
        component_name=data['component_name'],
        note=data.get('note', None),
        created_by=data.get('created_by', 0)
    )
    db.session.add(component)
    db.session.commit()
    return {"message": "Component created successfully"}, 201

# Read all Components
def get_components():
    components = Component.query.all()
    component_list = []
    for component in components:
        component_data = {
            "id": component.id,
            "component_name": component.component_name,
            "create_date": component.create_date,
            "created_by": component.created_by,
            "note": component.note
        }
        component_list.append(component_data)
    return {"components": component_list}

# Read a specific Component by ID
def get_component(component_id):
    component = Component.query.get(component_id)
    if component:
        component_data = {
            "id": component.id,
            "component_name": component.component_name,
            "create_date": component.create_date,
            "created_by": component.created_by,
            "note": component.note
        }
        return {"component": component_data}
    return {"message": "Component not found"}, 404

# Update a Component by ID
def update_component(component_id, new_component_json):
    data = new_component_json
    component = Component.query.get(component_id)
    if component:
        component.component_name = data.get('component_name', component.component_name)
        component.note = data.get('note', component.note)
        component.created_by = data.get('created_by', component.created_by)
        db.session.commit()
        return {"message": "Component updated successfully"}
    return {"message": "Component not found"}, 404

# Delete a Component by ID
def delete_component(component_id):
    component = Component.query.get(component_id)
    if component:
        db.session.delete(component)
        db.session.commit()
        return {"message": "Component deleted successfully"}
    return {"message": "Component not found"}, 404

##LOG

# Create a new Log
def create_log(data_json):
    data = data_json
    log = Log(
        user_id=data['user_id'],
        affected_user_id=data['affected_user_id'],
        event_id=data['event_id'],
        ip_address=data['ip_address']
    )
    db.session.add(log)
    db.session.commit()
    return {"message": "Log created successfully"}, 201

# Read all Logs
def get_logs():
    logs = Log.query.all()
    log_list = []
    for log in logs:
        log_data = {
            "id": log.id,
            "timestamp": log.timestamp,
            "user_id": log.user_id,
            "affected_user_id": log.affected_user_id,
            "event_id": log.event_id,
            "ip_address": log.ip_address
        }
        log_list.append(log_data)
    return {"logs": log_list}

# Read a specific Log by ID
def get_log(log_id):
    log = Log.query.get(log_id)
    if log:
        log_data = {
            "id": log.id,
            "timestamp": log.timestamp,
            "user_id": log.user_id,
            "affected_user_id": log.affected_user_id,
            "event_id": log.event_id,
            "ip_address": log.ip_address
        }
        return {"log": log_data}
    return {"message": "Log not found"}, 404

# Update a Log by ID
def update_log(log_id, new_log_json):
    data = new_log_json
    log = Log.query.get(log_id)
    if log:
        log.user_id = data.get('user_id', log.user_id)
        log.affected_user_id = data.get('affected_user_id', log.affected_user_id)
        log.event_id = data.get('event_id', log.event_id)
        log.ip_address = data.get('ip_address', log.ip_address)
        db.session.commit()
        return {"message": "Log updated successfully"}
    return {"message": "Log not found"}, 404

# Delete a Log by ID
def delete_log(log_id):
    log = Log.query.get(log_id)
    if log:
        db.session.delete(log)
        db.session.commit()
        return {"message": "Log deleted successfully"}
    return {"message": "Log not found"}, 404
