from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt
from app.routes.auth import auth_bp
from flask_cors import CORS
from app.routes.property import property_bp

from dotenv import load_dotenv
load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={
        r"/api/*": {
            "origins": [
                "http://localhost:5173",
                "      "
            ]
        }
    })
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(property_bp)

    return app
