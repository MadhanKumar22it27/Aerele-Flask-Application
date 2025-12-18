from flask import Blueprint, request, jsonify
from models import Resource
from database import db

resources_bp = Blueprint('resources', __name__)

@resources_bp.route('/', methods=['POST'])
def create_resource():
    data = request.get_json()

    # 1. Validate JSON exists
    if not data:
        return jsonify({"error": "Invalid or empty JSON"}), 400

    # 2. Safely read values
    name = data.get('name')
    resource_type = data.get('type')

    # 3. Validate required fields
    if not name or not resource_type:
        return jsonify({
            "error": "Both resource name and type are required"
        }), 400

    # 4. Create resource
    resource = Resource(
        name=name,
        type=resource_type
    )

    db.session.add(resource)
    db.session.commit()

    return jsonify({
        "message": "Resource created successfully",
        "resource_id": resource.id
    }), 201
