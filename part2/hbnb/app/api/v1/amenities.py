from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        # Placeholder for the logic to register a new amenity
        amenity_data = api.payload
        
        if not amenity_data:
            return {'message': 'Invalid input data'}, 400
        
        new_amenity = facade.create_amenity(amenity_data)
        return {
            "name": new_amenity.name
        }, 201
        
        

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Placeholder for logic to return a list of all amenities
        amenities = facade.get_all_amenities()
        return {'amenities': amenities}

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        # Placeholder for the logic to retrieve an amenity by ID
        amenities_data = facade.get_amenity(amenity_id)
        
        if not amenities_data:
            return  {'message': 'Amenity not found'}, 404
        return {
            "name": amenities_data.name
        }, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        # Placeholder for the logic to update an amenity by ID
        amenity_data = api.payload
        
        if not amenity_data:
             return {'message': 'Invalid input data'}, 400
         
        updated_amenities = facade.update_amenity(amenity_id, amenity_data)
        if not updated_amenities:
            return {'message': 'Amenity not found'}, 404
        return {
            "name": updated_amenities.name
        }