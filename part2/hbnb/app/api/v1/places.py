from flask_restx import Namespace, Resource, fields
from app import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('User', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})


# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner details'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.String, description="List of reviews ID's")
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        # Placeholder for the logic to register a new place
        place_data = api.payload
        
        if not place_data:
            return {'message': 'Invalid input data'}, 400
        owner_data = facade.get_user(place_data['owner_id'])
        
        place_data['owner'] = owner_data
        place_data.pop('owner_id')
        
        new_place = facade.create_place(place_data)

        return {
                    "id": new_place.id,
                    "title": new_place.title,
                    "description": new_place.description,
                    "price": new_place.price,
                    "latitude": new_place.latitude,
                    "longitude": new_place.longitude,
                    "owner": {
                        "id": owner_data.id,
                        "first_name": owner_data.first_name,
                        "last_name": owner_data.last_name,
                        "email": owner_data.email
                    }
                }, 201
        

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        places = facade.get_all_places()
        return [
            {
                "id": place.id,
                "title": place.title,
                "description": place.description,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner": place.owner
            } for place in places
        ]

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.expect(place_model)
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities

        place_data = facade.get_place(place_id)
        if not place_data:
            return {'message': 'Place not found'}, 404
        
        owner_data = facade.get_user(place_data.owner_id)
        if not owner_data:
            return {'message': 'Owner not found'}, 404

        return {
            "id": place_data.id,
            "title": place_data.title,
            "description": place_data.description,
            "price": place_data.price,
            "latitude": place_data.latitude,
            "longitude": place_data.longitude,
            "owner": {
                "id": place_data.owner_id,
                "first_name": owner_data.first_name,
                "last_name": owner_data.last_name,
                "email": owner_data.email
            }
        }, 200


    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        place_data = api.payload
        if not place_data:
            return {'message': 'Invalid input data'}, 400
    
        updated_place = facade.update_place(place_id, place_data)
        if not updated_place:
            return {'message': 'Place not found'}, 404
        
        return {
            "title": updated_place.title,
            "description": updated_place.description,
            "price": updated_place.price,
            "latitude": updated_place.latitude,
            "longitude": updated_place.longitude,
            "owner_id": updated_place.owner_id
            }, 200