from application import db
from application.models.locations import *

##LOCATION

# Create a new Location
def create_location(data_json):
    data = data_json
    location = Location(
        location_code=data['location_code'],
        location_name=data['location_name'],
        active=data.get('active', True),
        note=data.get('note', None),
        created_by=data.get('created_by', 0)
    )
    db.session.add(location)
    db.session.commit()
    return {"message": "Location created successfully"}, 201

# Read all Locations
def get_locations():
    locations = Location.query.all()
    location_list = []
    for location in locations:
        location_data = {
            "id": location.id,
            "location_code": location.location_code,
            "location_name": location.location_name,
            "active": location.active,
            "create_date": location.create_date,
            "created_by": location.created_by,
            "note": location.note
        }
        location_list.append(location_data)
    return {"locations": location_list}

# Read a specific Location by ID
def get_location(location_id):
    location = Location.query.get(location_id)
    if location:
        location_data = {
            "id": location.id,
            "location_code": location.location_code,
            "location_name": location.location_name,
            "active": location.active,
            "create_date": location.create_date,
            "created_by": location.created_by,
            "note": location.note
        }
        return {"location": location_data}
    return {"message": "Location not found"}, 404

# Update a Location by ID
def update_location(location_id, new_location_json):
    data = new_location_json
    location = Location.query.get(location_id)
    if location:
        location.location_code = data.get('location_code', location.location_code)
        location.location_name = data.get('location_name', location.location_name)
        location.active = data.get('active', location.active)
        location.note = data.get('note', location.note)
        location.created_by = data.get('created_by', location.created_by)
        db.session.commit()
        return {"message": "Location updated successfully"}
    return {"message": "Location not found"}, 404

# Delete a Location by ID
def delete_location(location_id):
    location = Location.query.get(location_id)
    if location:
        db.session.delete(location)
        db.session.commit()
        return {"message": "Location deleted successfully"}
    return {"message": "Location not found"}, 404

##BUILDING

# Create a new Building
def create_building(data_json):
    data = data_json
    building = Building(
        building_code=data['building_code'],
        building_name=data['building_name'],
        location_id=data['location_id'],
        active=data.get('active', True),
        note=data.get('note', None),
        created_by=data.get('created_by', 0)
    )
    db.session.add(building)
    db.session.commit()
    return {"message": "Building created successfully"}, 201

# Read all Buildings
def get_buildings():
    buildings = Building.query.all()
    building_list = []
    for building in buildings:
        building_data = {
            "id": building.id,
            "building_code": building.building_code,
            "building_name": building.building_name,
            "location_id": building.location_id,
            "active": building.active,
            "create_date": building.create_date,
            "created_by": building.created_by,
            "note": building.note
        }
        building_list.append(building_data)
    return {"buildings": building_list}

# Read a specific Building by ID
def get_building(building_id):
    building = Building.query.get(building_id)
    if building:
        building_data = {
            "id": building.id,
            "building_code": building.building_code,
            "building_name": building.building_name,
            "location_id": building.location_id,
            "active": building.active,
            "create_date": building.create_date,
            "created_by": building.created_by,
            "note": building.note
        }
        return {"building": building_data}
    return {"message": "Building not found"}, 404

# Update a Building by ID
def update_building(building_id, new_building_json):
    data = new_building_json
    building = Building.query.get(building_id)
    if building:
        building.building_code = data.get('building_code', building.building_code)
        building.building_name = data.get('building_name', building.building_name)
        building.location_id = data.get('location_id', building.location_id)
        building.active = data.get('active', building.active)
        building.note = data.get('note', building.note)
        building.created_by = data.get('created_by', building.created_by)
        db.session.commit()
        return {"message": "Building updated successfully"}
    return {"message": "Building not found"}, 404

# Delete a Building by ID
def delete_building(building_id):
    building = Building.query.get(building_id)
    if building:
        db.session.delete(building)
        db.session.commit()
        return {"message": "Building deleted successfully"}
    return {"message": "Building not found"}, 404


##ROOM

# Create a new Room
def create_room(data_json):
    data = data_json
    room = Room(
        room_code=data['room_code'],
        room_name=data['room_name'],
        building_id=data['building_id'],
        active=data.get('active', True),
        note=data.get('note', None),
        created_by=data.get('created_by', 0)
    )
    db.session.add(room)
    db.session.commit()
    return {"message": "Room created successfully"}, 201

# Read all Rooms
def get_rooms():
    rooms = Room.query.all()
    room_list = []
    for room in rooms:
        room_data = {
            "id": room.id,
            "room_code": room.room_code,
            "room_name": room.room_name,
            "building_id": room.building_id,
            "active": room.active,
            "create_date": room.create_date,
            "created_by": room.created_by,
            "note": room.note
        }
        room_list.append(room_data)
    return {"rooms": room_list}

# Read a specific Room by ID
def get_room(room_id):
    room = Room.query.get(room_id)
    if room:
        room_data = {
            "id": room.id,
            "room_code": room.room_code,
            "room_name": room.room_name,
            "building_id": room.building_id,
            "active": room.active,
            "create_date": room.create_date,
            "created_by": room.created_by,
            "note": room.note
        }
        return {"room": room_data}
    return {"message": "Room not found"}, 404

# Update a Room by ID
def update_room(room_id, new_room_json):
    data = new_room_json
    room = Room.query.get(room_id)
    if room:
        room.room_code = data.get('room_code', room.room_code)
        room.room_name = data.get('room_name', room.room_name)
        room.building_id = data.get('building_id', room.building_id)
        room.active = data.get('active', room.active)
        room.note = data.get('note', room.note)
        room.created_by = data.get('created_by', room.created_by)
        db.session.commit()
        return {"message": "Room updated successfully"}
    return {"message": "Room not found"}, 404

# Delete a Room by ID
def delete_room(room_id):
    room = Room.query.get(room_id)
    if room:
        db.session.delete(room)
        db.session.commit()
        return {"message": "Room deleted successfully"}
    return {"message": "Room not found"}, 404
