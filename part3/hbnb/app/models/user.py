import uuid
from datetime import datetime
from .__init__ import BaseModel, db, bcrypt

class User(BaseModel):

    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, first_name='', last_name='', email='', is_admin=False, password=''):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Si un mot de passe est fourni, le hacher avant de l'assigner
        if password:
            self.hash_password(password)

    def validation(self):
        """Valider les entrées de l'utilisateur avant de les enregistrer."""
        if len(self.first_name) > 50 or len(self.last_name) > 50:
            raise ValueError("Le prénom ou le nom de famille est trop long!")
        if not isinstance(self.is_admin, bool):
            raise ValueError("Le statut admin doit être un booléen!")
        # Vous pouvez ajouter d'autres validations ici si nécessaire

    def save(self):
        """Mettre à jour le timestamp `updated_at` lors de la modification de l'objet."""
        self.updated_at = datetime.now()

    def add_place(self, place):
        """Ajouter un lieu à l'utilisateur."""
        self.place.append(place)

    def hash_password(self, password):
        """Hacher le mot de passe avant de le stocker."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Vérifier le mot de passe haché."""
        return bcrypt.check_password_hash(self.password, password)
