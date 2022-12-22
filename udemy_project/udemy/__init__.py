from os import getenv
from flask import Flask,jsonify,request
import pymssql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from udemy import extensions
from flask import Blueprint
from flask_restx import Api as RestX_Api
from udemy.lectures.models import User,Course,Section,Lecture
from udemy.extensions import db,guard
from flask_praetorian import auth_required
from udemy.commands import lecturedata,sectiondata,coursedata

import click
from flask.cli import with_appcontext

from .users.v1 import open_api,auth_api


api_blueprint = Blueprint("api", __name__, url_prefix="/api")

# api_blueprint.register_blueprint(training_api_v1)

# initialize restx
rest_api = RestX_Api(
    api_blueprint,
    title="udemy"
)

rest_api.add_namespace(open_api,path='/v1')
rest_api.add_namespace(auth_api,path='/v1')


def create_app():   #or make_app()
    app = Flask(__name__)

    app.config.from_object(get_config_object_path())

    app.register_blueprint(api_blueprint)


     # initializing all extensions
    extensions.init_extensions(app)
    extensions.guard.init_app(app,User)
    
    @app.route('/')
    def home():
        return "<h2>Hello world!! Welcome to Home Page <h2>"


    app.cli.add_command(lecturedata)
    app.cli.add_command(sectiondata)
    app.cli.add_command(coursedata)
        
    return app


def get_config_object_path():
    dev_config = "udemy.config.DevelopmentConfig"
    env = getenv('FLASK_ENV')
    environment_config = dev_config
    if env == 'developement':
        environment_config = dev_config
    
    return environment_config

