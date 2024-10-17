from flask_restx import Namespace, Resource, fields
from services.facade import HBnBFacade
from flask import request

api = Namespace('amenities', description='Opérations sur les commodités')

# Modèle de commodité pour la validation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Nom de la commodité')
})

facade = HBnBFacade()

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Commodité créée avec succès')
    @api.response(400, 'Données invalides')
    def post(self):
        """Créer une nouvelle commodité"""
        amenity_data = request.json
        result = facade.create_amenity(amenity_data)
        return result, 201

    @api.response(200, 'Liste des commodités récupérée')
    def get(self):
        """Récupérer toutes les commodités"""
        return facade.get_all_amenities()

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Commodité récupérée')
    @api.response(404, 'Commodité non trouvée')
    def get(self, amenity_id):
        """Récupérer une commodité par ID"""
        amenity = facade.get_amenity(amenity_id)
        if amenity:
            return amenity
        api.abort(404, 'Commodité non trouvée')

    @api.expect(amenity_model)
    @api.response(200, 'Commodité mise à jour')
    @api.response(404, 'Commodité non trouvée')
    @api.response(400, 'Données invalides')
    def put(self, amenity_id):
        """Mettre à jour une commodité par ID"""
        amenity_data = request.json
        result = facade.update_amenity(amenity_id, amenity_data)
        if result:
            return {"message": "Commodité mise à jour avec succès"}, 200
        api.abort(404, 'Commodité non trouvée')
