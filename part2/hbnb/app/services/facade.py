from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if user:
            user.first_name = user_data['first_name']
            user.last_name = user_data['last_name']
            user.email = user_data['email']
            self.user_repo.update(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def create_place(self, place_data):
        # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        pass

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        pass
    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass
