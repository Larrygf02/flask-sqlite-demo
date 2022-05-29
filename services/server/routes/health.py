from flask import Blueprint, jsonify

router = Blueprint('health', __name__, url_prefix='/health')

@router.route('/', methods=['GET'])
def health():
    data = {
        'status': 'UP'
    }
    return jsonify(data)
