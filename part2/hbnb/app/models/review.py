import uuid
from app.models.__init__ import BaseModel
from datetime import datetime
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity



class Review:
    def __init__(self, text, rating, place, user):

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
            "place_id": self.place,
            "user_id": self.user,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }