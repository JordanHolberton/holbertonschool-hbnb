from app.persistence.repository import InMemoryRepository
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Method for creating a user
    def create_user(self, user_data):
        user_id = user_data.get('id')
        if user_id and not self.user_repo.get(user_id):
            self.user_repo.add(user_id, user_data)
            return user_data
        return None
    
    # Method for fetching a place by ID
    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def create_review(self, review_data):
        # Extract required data from review_data
        user_id = review_data.get('user_id')
        place_id = review_data.get('place_id')
        text = review_data.get('text')
        rating = review_data.get('rating')
        
        # Ensure user_id, place_id, text, and rating are not None
        if not user_id or not place_id or not text or rating is None:
            return None
        
        # Validate that user and place exist
        user = self.user_repo.get(user_id)
        place = self.place_repo.get(place_id)
        if not user or not place:
            return None
        
        # Validate the rating is between 1 and 5
        if not (1 <= rating <= 5):
            return None

        # Create review object
        review_id = f'review_{len(self.review_repo.data) + 1}'
        review = {
            'id': review_id,
            'text': text,
            'rating': rating,
            'user_id': user_id,
            'place_id': place_id
        }

        # Add the review to the repository
        self.review_repo.add(review_id, review)
        return review, None

    def get_review(self, review_id):
        # Retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Retrieve all reviews for a specific place
        reviews = [review for review in self.review_repo.data.values() if review['place_id'] == place_id]
        return reviews if reviews else None

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None, "Review not found"

        # Only update fields that are provided
        if 'text' in review_data:
            review['text'] = review_data['text']
        if 'rating' in review_data:
            if not (1 <= review_data['rating'] <= 5):
                return None, "Rating must be between 1 and 5"
            review['rating'] = review_data['rating']
        
        # Save updated review
        self.review_repo.update(review_id, review)
        return review, None

    def delete_review(self, review_id):
        # Delete a review by ID
        return self.review_repo.delete(review_id)