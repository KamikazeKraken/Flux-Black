from flask import Flask
import jinja_partials

import helpers
import os


__all__ = ["create_app"]


def create_app(config_file: str) -> Flask:
    app = Flask(
        __name__,
        template_folder=helpers.TEMPLATE_DIR,
        static_folder=helpers.STATIC_DIR
    )
    
    app.secret_key = os.getenv("FLASK_SECRET_KEY")
    jinja_partials.register_extensions(app)
    helpers.config_loader(config_file).apply(app)
    
    return app