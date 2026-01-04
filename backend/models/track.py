from extensions import db
from datetime import datetime

class Track(db.Model):
    __tablename__ = "tracks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    artist = db.Column(db.String(100))
    category = db.Column(db.String(50))
    file_path = db.Column(db.String(255), nullable=False)

    is_podcast = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
