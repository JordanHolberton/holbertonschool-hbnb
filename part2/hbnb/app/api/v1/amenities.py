#!/usr/bin/python3
"""
API pour la gestion des commodités (amenities).
Cette API permet de créer, consulter et mettre à jour des commodités,
tout en respectant le pattern Facade pour la gestion de la logique métier.
"""

from flask import request
from flask_restx import Namespace, Resource, fields
from datetime import datetime
from services.facade import HBnBFacade  # Assurez-vous que cette classe suit le pattern Facade.
import uuid

# Namespace Flask-RESTx pour les opérations liées aux commodités
ns = Namespace('amenities', description='Opérations sur les commodités')

# Instance du Facade pour gérer la logique métier
facade = HBnBFacade()

# Définition du modèle de commodité pour la validation des entrées et la documentation
amenity_model = ns.model('Amenity', {
    'id': fields.String(
        required=True,
        description='ID unique de la commodité'
    ),
    'name': fields.String(
        required=True,
        description='Nom de la commodité'
    ),
    'created_at': fields.DateTime(
        required=True,
        description='Date de création de la commodité'
    ),
    'updated_at': fields.DateTime(
        required=True,
        description='Dernière date de mise à jour de la commodité'
    )
})


@ns.route('/')
class Amenities(Resource):
    """Gestion des commodités : Création et récupération de toutes les commodités."""

    @ns.marshal_list_with(amenity_model)
    def get(self):
        """
        Récupérer la liste de toutes les commodités.
        Renvoie un tableau contenant toutes les commodités disponibles.
        """
        return facade.get_all_amenities()

    @ns.expect(amenity_model)
    @ns.response(201, 'Commodité créée avec succès')
    @ns.response(400, 'Requête invalide')
    def post(self):
        """
        Créer une nouvelle commodité.
        Génère un ID unique et enregistre la nouvelle commodité avec des informations de création.
        """
        new_amenity_data = request.json
        new_amenity_data['id'] = str(uuid.uuid4())  # Génération d'un ID unique
        new_amenity_data['created_at'] = datetime.now()  # Date de création
        new_amenity_data['updated_at'] = datetime.now()  # Date de mise à jour
        amenity_id = facade.create_amenity(new_amenity_data)  # Enregistrement via la couche Facade
        return {
            'message': 'Commodité créée avec succès',
            'amenity_id': amenity_id
        }, 201


@ns.route('/<string:amenity_id>')
class AmenityResource(Resource):
    """Gestion d’une commodité spécifique : Consultation et mise à jour."""

    @ns.marshal_with(amenity_model)
    @ns.response(404, 'Commodité non trouvée')
    def get(self, amenity_id):
        """
        Récupérer une commodité par son ID.
        Renvoie les détails de la commodité ou un message d’erreur si non trouvée.
        """
        amenity_data = facade.get_amenity(amenity_id)
        if amenity_data:
            return amenity_data
        else:
            ns.abort(404, "Commodité non trouvée")

    @ns.expect(amenity_model)
    @ns.response(200, 'Commodité mise à jour avec succès')
    @ns.response(400, 'Requête invalide')
    @ns.response(404, 'Commodité non trouvée')
    def put(self, amenity_id):
        """
        Mettre à jour une commodité existante.
        Modifie les informations de la commodité avec l’ID spécifié.
        """
        updated_data = request.json
        updated_data['id'] = amenity_id  # Conserver l’ID d'origine
        updated_data['updated_at'] = datetime.now()  # Mettre à jour la date de modification
        if facade.update_amenity(amenity_id, updated_data):
            return {'message': 'Commodité mise à jour avec succès'}, 200
        else:
            ns.abort(404, "Commodité non trouvée")