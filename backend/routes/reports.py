from flask import Blueprint, request, jsonify
from models import Resource, Event, EventResourceAllocation
from database import db
from datetime import datetime

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/utilization', methods=['GET'])
def resource_utilization():
    start = datetime.fromisoformat(request.args.get('start'))
    end = datetime.fromisoformat(request.args.get('end'))

    report = []

    for resource in Resource.query.all():
        total_hours = 0

        allocations = db.session.query(Event).join(EventResourceAllocation).filter(
            EventResourceAllocation.resource_id == resource.id,
            Event.start_time < end,
            Event.end_time > start
        ).all()

        for event in allocations:
            effective_start = max(event.start_time, start)
            effective_end = min(event.end_time, end)
            total_hours += (effective_end - effective_start).total_seconds() / 3600

        report.append({
            "resource": resource.name,
            "total_hours": round(total_hours, 2)
        })

    return jsonify(report)
