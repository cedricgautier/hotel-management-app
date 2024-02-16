from dotenv import load_dotenv
from flask import Flask
from .routes import main as main_routes
from .database import initialize_db_config
from .blueprints import register_blueprints


# from flask_login import LoginManager
def init_env():
    load_dotenv()


def create_app():
    app = Flask(__name__)
    initialize_db_config(app)
    register_blueprints(app, main_routes)
    return app
