from flask import Flask
from config import Config
from extensions import cors, jwt, db
from routes.auth_routes import auth_bp
from models.user import User    

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return {"message": "Music & Podcast API is running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
