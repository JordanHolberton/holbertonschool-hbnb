import uuid
from datetime import datetime
from app.models.place import Place
from app.models.review import Review

class User:
    def __init__(self, first_name='', last_name='', email='', is_admin=False):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

def validation(self, first_name, last_name, is_admin):
        if len(self.first_name) > 50 or len(self.last_name) > 50:
            raise ValueError("First name or last name is too long!")
        if not isinstance(self.is_admin, bool):
            raise ValueError("Must be admin!")
        self.first_name = first_name
        self.last_name = last_name


def add_place(self, review):
    """Add a review to the place."""
    self.place.append(place)
