from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints (to be added later)
    # from app.routes import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app