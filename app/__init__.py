from flask import Flask
from app import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    
    from app.home.routes import home
    app.register_blueprint(home)

    return app
