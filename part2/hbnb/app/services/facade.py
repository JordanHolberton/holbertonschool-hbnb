from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        return self.place_repo.get(place_id)

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        place = self.place_repo.get(place_id)
        place.update(place_data)
        self.place_repo.update(place)
        if place:
            place.title = place_data['title']
            place.description = place_data['description']
            place.price = place_data['price']
            place.latitude = place_data['latitude']
            place.longitude = place_data['longitude']
            place.owner_id = place_data['owner_id']
            self.place_repo.update(place)
        return place
