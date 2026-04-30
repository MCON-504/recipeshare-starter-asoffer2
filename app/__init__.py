from flask import Flask

from .config import Config
from .extensions import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    app.register_blueprint(main) # all routes to one blueprint - instead of @app, do @blueprint

    return app
