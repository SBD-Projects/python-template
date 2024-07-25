from flask import Blueprint, request, jsonify, abort
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from flask_cors import CORS, cross_origin

user_blueprint = Blueprint('user_blueprint', __name__)
CORS(user_blueprint)
# Instantiate the service with the repository
user_repository = UserRepository()
user_service = UserService(user_repository)

@user_blueprint.route('/register', methods=['POST'])
@cross_origin()
def create_user():
    print(request.get_json())
    user_data = request.get_json()
    try:
        user = user_service.create_user(user_data)
    except Exception as e:
        print(e)  # For debugging
        abort(400, str(e))
    return jsonify(user.id), 201

@user_blueprint.route('/login', methods=['POST'])
@cross_origin()
def login():
    user_data = request.get_json()
    email = user_data.get('email')
    password = user_data.get('password')
    
    user = user_service.get_by_email(email)
    if not user or not check_password_hash(user.password, password):
        abort(401, 'Invalid email or password')

    access_token = create_access_token(identity={'id': user.id, 'email': user.email})
    return jsonify(access_token=access_token), 200

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = user_service.get_by_id(user_id)
    if not user:
        abort(404)
    return jsonify(user_id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email, phone_number=user.phone_number, date_of_birth=user.date_of_birth), 200

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    success = user_service.delete_by_id(user_id)
    if not success:
        abort(404)
    return jsonify(success=True), 200

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    update_data = request.get_json()
    user = user_service.update_info_by_id(user_id, update_data)
    if not user:
        abort(404)
    return jsonify(user_id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email, phone_number=user.phone_number, date_of_birth=user.date_of_birth), 200
