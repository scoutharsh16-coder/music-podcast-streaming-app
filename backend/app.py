from flask import Flask
from config import Config
from extensions import cors, jwt, db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    @app.route("/")
    def home():
        return {"message": "Music & Podcast API is running"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
