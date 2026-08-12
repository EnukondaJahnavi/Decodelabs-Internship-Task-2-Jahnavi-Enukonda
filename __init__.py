from flask import Flask
from flask_cors import CORS
from .routes import api
from .errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(api, url_prefix="/api")
    register_error_handlers(app)

    @app.get("/")
    def home():
        return {
            "success": True,
            "message": "DecodeLabs Project 2 - Backend API is running",
            "api": "/api",
            "documentation": "/api/docs"
        }, 200

    return app
