from __init__ import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = [] # List to store related amenities
        self.users = []

    def title(self, title):
        if len(title) > 100:
            raise TypeError("Error: title is invalid")
        self.title = title
        
    def descritption(self, description):
        self.description = description
        
    def price(self, price):
        if price < 0:
            raise ValueError("Price can't negatif")
        self.price = price
        
    def coordinate(self, latitude, longitude):
        if not -90 <= latitude <= 90 or -180 <= longitude <= 180:
            raise ValueError(" coordinate of latitude and longitude aren't correct")
        self.latitude = latitude
        self.longitude = longitude

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
        
    def add_user(self, user):
        """Add an user to the place"""
        self.users.append(user)
