from app.persistence.repository import SQLAlchemyRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_all_users(self):
        return self.user_repo.get_all()

    def updated_user(self, user_id, user_data):
        # Fetch the user by their ID
        user = self.user_repo.get(user_id)
        
        if not user:
            # Return None or handle the case where the user doesn't exist
            return None
        
        # Update the user's details only if the data is provided in the request
        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        
        if 'email' in user_data:
            user.email = user_data['email']
        
        # Persist the changes to the repository
        self.user_repo.update(user, user_data)
        
        return user

    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        amenity = self.get_amenity(amenity_id)
        if amenity:
            if 'name' in amenity_data:
                amenity.name = amenity_data['name']
            self.amenity_repo.update(amenity, amenity_data)
        return amenity


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
        if place:
            if 'title' in place_data:
                place.title = place_data['title']
            if 'description' in place_data:
                place.description = place_data['description']
            if 'price' in place_data:
                place.price = place_data['price']
            if 'latitude' in place_data:
                place.latitude = place_data['latitude']
            if 'longitude' in place_data:
                place.longitude = place_data['longitude']
            if 'owner_id' in place_data:
                place.owner_id = place_data['owner_id']
            self.place_repo.update(place, place_data)
        return place
    
    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        return self.review_repo.get(place_id)
    
    def get_review_by_user_and_place(self, user_id, place_id):
        return Review.query.filter_by(user_id=user_id, place_id=place_id).first()

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review

        review = self.get_review(review_id)
        if not review:
            raise ValueError("Review not found")

        self.review_repo.update(review_id, review_data)
        return self.get_review(review_id)

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        review = self.review_repo.get(review_id)
        if review:
            self.review_repo.delete(review_id)
            return {'message': 'Review deleted sucessfully'}