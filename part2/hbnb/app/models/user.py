import uuid
from datetime import datetime

class User:
    def __init__(self, username, password, is_admin=False):

        if not username or len(username) > 50:
            raise ValueError("Username is required and must be at most 50 characters long.")
        self.username = username
        
        if not password or len(password) < 6:
            raise ValueError("Password is required and must be at least 6 characters long.")
        self.password = password

        if not isinstance(is_admin, bool):
            raise ValueError("Admin status must be a boolean.")
        self.is_admin = is_admin

        self.id = str(uuid.uuid4())

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
