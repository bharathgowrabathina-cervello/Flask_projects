"""Entrypoint for the base application.
Returns:
    Flask: Flask app instance
"""

from os import getenv
from flask import Flask,jsonify,request
import pymssql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from udemy import extensions
from flask import Blueprint
from flask_restx import Api as RestX_Api

# # NOTE: It's important to import the models here for sql-alchemy to recognize
from udemy.lectures.models import User,Course,Section,Lecture

from udemy.extensions import db,guard
from flask_praetorian import auth_required
from udemy.commands import lecturedatac,sectiondatac,coursedatac,deploy,command_code

import click
from flask.cli import with_appcontext

from .users.v1 import open_api,auth_api


api_blueprint = Blueprint("api", __name__, url_prefix="/api")


# initialize restx
rest_api = RestX_Api(
    api_blueprint,
    title="udemy"
)

# add namespaces to restx
rest_api.add_namespace(open_api,path='/v1')
rest_api.add_namespace(auth_api,path='/v1')


import logging

# Create and configure logging file
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:/Users/gkumar01/OneDrive - Kearney/Documents/udemy_logs.log",level=logging.DEBUG,format=LOG_FORMAT)


# entry point of the flask application
def create_app():   
    """Create the flask app and intialize all the extensions"""
    
    app = Flask(__name__)

    app.config.from_object(get_config_object_path())

    app.register_blueprint(api_blueprint)


     # initializing all extensions
    extensions.init_extensions(app)
    
    # praetorian (JWT token) intialize
    extensions.guard.init_app(app,User)
    
    @app.route('/')
    def home():
        return "<h2>Hello world!! Welcome to Home Page <h2>"

    # custom management commands
    # app.cli.add_command(lecturedatac)
    # app.cli.add_command(sectiondatac)
    # app.cli.add_command(coursedatac)
    # app.cli.add_command(deploy)
    app.cli.add_command(command_code)
        
    return app


def get_config_object_path():
    """reads `FLASK_ENV` from OS and returns string that can be used with app.config.from_object.
    If `FLASK_ENV` not set in OS, returns `base.config.DevelopmentConfig`
    Returns:
        str: one of 'base.config.DevelopmentConfig', 'base.config.TestingConfig', 'base.config.ProductionConfig'
    """
    
    dev_config = "udemy.config.DevelopmentConfig"
    env = getenv('FLASK_ENV')
    environment_config = dev_config
    if env == 'developement':
        environment_config = dev_config
    
    return environment_config

