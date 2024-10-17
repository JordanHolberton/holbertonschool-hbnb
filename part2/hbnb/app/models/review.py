import uuid
from datetime import datetime
from models.place import Place

class Review:
    def __init__(self, text, rating, place, user):
        from models.user import User
        
        if not text:
            raise ValueError("Review text is required")
        self.text = text


        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.rating = rating

        if not isinstance(place, Place):
            raise ValueError("Invalid Place")
        self.place = place


        if not isinstance(user, User):
            raise ValueError("Invalid User")
        self.user = user

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "place_id": self.place.id,
            "user_id": self.user.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
