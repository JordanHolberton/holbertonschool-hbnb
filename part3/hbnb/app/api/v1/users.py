from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask_jwt_extended import jwt_required, get_jwt_identity
import re
from flask import request

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    @jwt_required()
    def post(self):
        """Register a new user"""
        current_user = get_jwt_identity()
        if current_user.get('is_admin', True):
            is_admin = facade.get_user(current_user['id']).is_admin
            if not is_admin:
                return {'error': 'Admin privileges required'}, 403
        else:
            return {'error': 'Admin privileges required'}, 403
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        if not user_data or not isinstance(user_data, dict):
            return {'error': 'Invalid input data'}, 400
        if not user_data.get('first_name') or not user_data.get('last_name'):
            return {'error': 'Invalid input data'}, 400
        # Validate email format (basic regex for example purposes)
        email = user_data.get('email')
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return {'error': 'Invalid email format'}, 400

        new_user = facade.create_user(user_data)
        {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email,
            'password': new_user.password
        }

        return {'id': new_user.id, "message": 'User Successfully created'}, 201
    
        

    @api.response(200, "List of users successfully retrieved")
    def get(self):
        """Retrieve list of users"""
        users = facade.get_all_users()
        return [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            } for user in users
        ]


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            }, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User sucessfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Unauthorized action')
    @jwt_required()
    def put(self, user_id):
        """Update user informations"""
        user_data = api.payload
        current_user = get_jwt_identity()

        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        data = request.json
        email = data.get('email')

        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400
        user = facade.get_user(user_id)

        if user != current_user:
            return {'error': 'Unauthorized action'}, 403
        if not user:
            return {'error': 'User not found'}, 404
        
        if 'email' in user_data or 'password' in user_data:
            return {'error': 'You cannot modify email of password'}, 403

        updated_user = facade.updated_user(user_id, user_data)
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email,
            'password': updated_user.password
        }, 200
