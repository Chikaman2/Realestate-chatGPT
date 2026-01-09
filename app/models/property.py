from app.extensions import db
from datetime import datetime, UTC

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric)
    location = db.Column(db.String(150))
    image_url = db.Column(db.String(300))
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(UTC))
