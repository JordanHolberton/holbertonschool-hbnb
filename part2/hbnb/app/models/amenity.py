import uuid
from datetime import datetime


class Amenity:
    def __init__(self, name):
        # Vérification du Nom
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and must be at most 50 characters long.")
        self.name = name

        # Génération d'un ID unique
        self.id = str(uuid.uuid4())

        # Heure création et mise à jour
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        # Mise à jour heure
        self.updated_at = datetime.now()

    def dict(self):
        # Retourne un dictionnaire avec les informations
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
