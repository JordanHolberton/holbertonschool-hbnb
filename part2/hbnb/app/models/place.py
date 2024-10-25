import uuid
from datetime import datetime
from app.models.__init__ import BaseModel

class Place(BaseModel):
    def __init__(self, title='', description='', price='', latitude='', longitude='', owner={}, id=None, amenities=[]):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) > 100:
            raise TypeError("Error: title is invalid")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self._price = value

    def set_coordinates(self, latitude, longitude):
        if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
            raise ValueError("Coordinates of latitude and longitude aren't correct")
        self._latitude = latitude
        self._longitude = longitude

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def add_user(self, user):
        """Add a user to the place"""
        self.users.append(user)

    def to_dict(self):
        """Convert the Place object to a dictionary."""
        return {
            'id': self.id,
            'title': self._title,
            'description': self._description,
            'price': self._price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'reviews': self.reviews,
            'amenities': self.amenities,
            'users': self.users
        }