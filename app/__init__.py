from flask import Flask
from flask_migrate import Migrate
from app.routes.user_routes import user_blueprint
from app.utils.database import init_db
from flask_cors import CORS
from app.utils.jwt_utils import init_jwt

def create_app():
    app = Flask(__name__)
    CORS(app)
    init_db(app)

    init_jwt(app)

    app.register_blueprint(user_blueprint)
    return app
