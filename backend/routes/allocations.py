from flask import Blueprint, request, jsonify
from models import Event, Resource, EventResourceAllocation
from database import db

allocations_bp = Blueprint('allocations', __name__)

def has_conflict(resource_id, start, end, event_id=None):
    query = db.session.query(Event).join(EventResourceAllocation).filter(
        EventResourceAllocation.resource_id == resource_id,
        Event.start_time < end,
        Event.end_time > start
    )

    if event_id:
        query = query.filter(Event.id != event_id)

    return query.first() is not None

@allocations_bp.route('/', methods=['POST'])
def allocate_resource():
    data = request.json
    event_id = data['event_id']
    resource_id = data['resource_id']

    event = Event.query.get_or_404(event_id)

    if has_conflict(resource_id, event.start_time, event.end_time, event_id):
        return jsonify({
            "error": "Resource already booked for overlapping time"
        }), 400

    allocation = EventResourceAllocation(
        event_id=event_id,
        resource_id=resource_id
    )

    db.session.add(allocation)
    db.session.commit()

    return jsonify({"message": "Resource allocated successfully"})
