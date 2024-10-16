import uuid
from datetime import datetime

class Review:
    def __init__(self, text, rating, place, user):
        # Vérif du Texte
        if not text:
            raise ValueError("Review text is required")
        self.text = text

        # Vérif du Rating
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.rating = rating

        # Vérif de la véracité de Place
        if not isinstance(place, Place):
            raise ValueError("Invalid Place")
        self.place = place

        # Vérif du User s'il existe
        if not isinstance(user, User):
            raise ValueError("Invalid User")
        self.user = user

        # Suivi temporel de la classe reviex 
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        # Checker de l'heure et la date
        self.updated_at = datetime.now()

    def dict(self):
        # Retourne un dictionnaire des infos
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "place_id": self.place,
            "user_id": self.user,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
