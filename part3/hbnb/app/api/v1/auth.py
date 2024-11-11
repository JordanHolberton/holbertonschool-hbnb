from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('auth', description='Authentication operations')

# Modèle pour la validation des données d'entrée (login)
login_model = api.model('Login', {
    'email': fields.String(required=True, description='L\'email de l\'utilisateur'),
    'password': fields.String(required=True, description='Le mot de passe de l\'utilisateur')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)  # Utilise le modèle pour valider les données envoyées dans la requête
    def post(self):
        """Authentifie l'utilisateur et retourne un token JWT"""
        credentials = api.payload  # Récupère les informations de connexion (email, mot de passe) envoyées par le client
        
        # Étape 1 : Récupérer l'utilisateur avec l'email fourni
        user = facade.get_user_by_email(credentials['email'])
        
        # Étape 2 : Vérifier si l'utilisateur existe et si le mot de passe est correct
        if not user:
            # Si l'utilisateur n'est pas trouvé, renvoie une erreur 404
            return {'error': 'Utilisateur non trouvé'}, 404
        if not user.verify_password(credentials['password']):
            # Si le mot de passe est incorrect, renvoie une erreur 401
            return {'error': 'Mot de passe incorrect'}, 401

        # Étape 3 : Créer un token JWT avec l'id de l'utilisateur et son rôle (is_admin)
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        
        # Étape 4 : Retourner le token JWT au client
        return {'access_token': access_token}, 200

@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()  # Protège cette route, l'accès nécessite un token JWT valide
    def get(self):
        """Une route protégée qui nécessite un token JWT valide"""
        current_user = get_jwt_identity()  # Récupère l'identité de l'utilisateur depuis le token JWT
        # Retourne un message contenant l'ID de l'utilisateur authentifié
        return {'message': f'Bonjour, utilisateur {current_user["id"]}'}, 200
