from flask import Flask
from app.configs import database, migration, jwt_auth
from app.routes import init_app

def create_app():
    app = Flask(__name__)
    database.init_app(app)
    migration.init_app(app)
    jwt_auth.init_app(app)

    init_app(app)



    return app