# Flask Imports
from flask import Flask, url_for

# Third Party Imports
from dotenv import load_dotenv

# Standard Library Imports
import os

# Local Imports
import helpers
from helpers import LinkItem
import blueprints


# Load Environment Variables
load_dotenv(helpers.ROOT_DIR / ".env")


# Create Flask Application
app = helpers.create_app("config.json")


# Inject Global Data
@app.context_processor
def inject_globals():
    root_navigation = [
        LinkItem("Home", url_for("root.index")),    
        LinkItem("Socials", url_for("root.index")),    
        LinkItem("Projects", url_for("root.index")),    
        LinkItem("Blog", url_for("root.index")),    
        LinkItem("Admin", url_for("root.index")),    
    ]
    return {
        "current_hear": helpers.current_year,
        "landing_page": url_for("root.landing"),
        "root_navigation": root_navigation,
    }


app.register_blueprint(blueprints.root)