from app.extensions import db
from datetime import time, date
from sqlalchemy.types import Enum

class Resource(db.Model):
    """Base class for reservable resources."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    available = db.Column(db.Boolean, default=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # Differentiates resource types
    day = db.Column(db.Date, nullable=False, default=date.today)
    hour_from = db.Column(db.Time, nullable=False)
    hour_to = db.Column(db.Time, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'resource',
        'polymorphic_on': type
    }

class MeetingRoom(Resource):
    """Model for meeting rooms."""
    id = db.Column(db.Integer, db.ForeignKey('resource.id'), primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'meeting_room'
    }

class EquipmentType(Enum):
    """Enum for equipment types."""
    WINDOWS_LAPTOP = "Windows Laptop"
    MAC_LAPTOP = "Mac Laptop"
    MOUSE = "Mouse"
    KEYBOARD = "Keyboard"
    MONITOR = "Monitor"
    PRINTER = "Printer"

class Equipment(Resource):
    """Model for equipment."""
    id = db.Column(db.Integer, db.ForeignKey('resource.id'), primary_key=True)
    brand = db.Column(db.String(100), nullable=True)
    equipment_type = db.Column(Enum(EquipmentType), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'equipment'
    }

class TrainingSession(Resource):
    """Model for training sessions."""
    id = db.Column(db.Integer, db.ForeignKey('resource.id'), primary_key=True)
    instructor = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes

    __mapper_args__ = {
        'polymorphic_identity': 'training_session'
    }