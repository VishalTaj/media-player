from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from ddtrace import patch_all

db = SQLAlchemy()
migrate = Migrate()
# patch_all()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('settings.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes, models # Import routes
        # db.create_all()  # Create sql tables for our data models

        return app