from helpers import ROOT_DIR
from flask import Flask
import json


class config_loader:
    """
    Loads JSON data into a Flask Application's config dictionary.
    
    Parameters 
    ----------
    path : str
        The path to the config file, relative to the project root.
    app : Flask
        A Flask application instance.

    Usage:
    from flask import Flask
    import helpers

    app = Flask(__name__)
    helpers.config_loader("config.json").apply(app)
    """

    def __init__(self, path: str) -> None:
        """
        Iniitializes the class and loads the JSON data from the config file.
        """

        with open(ROOT_DIR / path, "r") as f:
            self.data = json.load(f)

    def apply(self, app: Flask) -> None:
        """
        Injects the JSON data into the flask application configuration.
        """

        app.config.update(self.data)