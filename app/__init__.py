import os
from flask import Flask
from config import config
from app.api.cache import cache

def create_app():
    app = Flask(os.getenv('APP_NAME'))
    app.config.from_object(config)   
    # cache.init_app(app)

    return app