from flask import Blueprint, jsonify
from models.track import Track

track_bp = Blueprint("tracks", __name__, url_prefix="/api/tracks")

@track_bp.route("/music", methods=["GET"])
def get_music():
    tracks = Track.query.filter_by(is_podcast=False).all()

    result = []
    for track in tracks:
        result.append({
            "id": track.id,
            "title": track.title,
            "artist": track.artist,
            "category": track.category
        })

    return jsonify(result)

@track_bp.route("/podcasts", methods=["GET"])
def get_podcasts():
    podcasts = Track.query.filter_by(is_podcast=True).all()

    result = []
    for p in podcasts:
        result.append({
            "id": p.id,
            "title": p.title,
            "artist": p.artist,
            "category": p.category
        })

    return jsonify(result)
