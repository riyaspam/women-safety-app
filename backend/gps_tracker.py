# gps_tracker.py
from models import db, Location


def save_location(user_id, lat, lon):
loc = Location(user_id=user_id, latitude=str(lat), longitude=str(lon))
db.session.add(loc)
db.session.commit()
return loc.id
