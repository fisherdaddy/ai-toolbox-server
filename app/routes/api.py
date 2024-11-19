from flask import Blueprint, jsonify
from app.services.some_service import SomeService

api_bp = Blueprint('api', __name__)

@api_bp.route('/example', methods=['GET'])
def example_endpoint():
    service = SomeService()
    result = service.get_example_data()
    return jsonify(result) 