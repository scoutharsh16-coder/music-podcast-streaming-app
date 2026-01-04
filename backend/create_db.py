from app import app
from extensions import db
from models.track import Track

with app.app_context():
    t1 = Track(
        title="Kesariya",
        artist="Arijit Singh",
        category="Bollywood",
        file_path="media/kesariya.mp3",
        is_podcast=False
    )

    t2 = Track(
        title="Tech Talks Ep 1",
        artist="Python Podcast",
        category="Technology",
        file_path="media/techtalk1.mp3",
        is_podcast=True
    )

    db.session.add_all([t1, t2])
    db.session.commit()
