from extensions import db

playlist_tracks = db.Table(
    "playlist_tracks",
    db.Column("playlist_id", db.Integer, db.ForeignKey("playlists.id")),
    db.Column("track_id", db.Integer, db.ForeignKey("tracks.id"))
)

class Playlist(db.Model):
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
