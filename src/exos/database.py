import os, logging
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.DEBUG)

db = SQLAlchemy()


def initialize_db_config(app):
    secret, db_uri = insert_app_variables()
    app.config["SECRET_KEY"] = secret
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    Migrate().init_app(app, db)


def insert_app_variables():
    secret = os.getenv("SECRET_KEY")
    if not secret:
        logging.fatal("err, insert_app_variables - unable to get secret key")
        return "", ""

    db_uri = os.getenv("DB_URI")
    if not db_uri:
        logging.fatal("err, insert_app_variables - unable to get db uri")
        return "", ""

    return secret, db_uri
