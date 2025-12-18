from flask import Blueprint, request, jsonify
from models import Event
from database import db
from dateutil.parser import parse

events_bp = Blueprint('events', __name__)

@events_bp.route('/', methods=['POST'])
def create_event():
    data = request.json

    start = parse(data['start_time'])
    end = parse(data['end_time'])

    if start >= end:
        return jsonify({"error": "Start time must be before end time"}), 400

    event = Event(
        title=data['title'],
        start_time=start,
        end_time=end,
        description=data.get('description')
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({"message": "Event created", "event_id": event.id})

@events_bp.route('/', methods=['GET'])
def list_events():
    events = Event.query.all()
    return jsonify([
        {
            "id": e.id,
            "title": e.title,
            "start": e.start_time,
            "end": e.end_time
        } for e in events
    ])
