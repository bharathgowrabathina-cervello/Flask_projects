"""Initialize 3-party libraries here.
Any 3-party Library or Extension can be initialized here. Flask follows factory pattern
Further Reads Flask Factory patterns: https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app as app
from flask_praetorian import Praetorian
from flask_marshmallow import Marshmallow
from flask_caching import Cache

db=SQLAlchemy()
migrate=Migrate()
guard=Praetorian()
ma=Marshmallow()
cache=Cache()

def init_extensions(app):

    with app.app_context():

        # sql-alchemy
        db.init_app(app)
        
        # migrations
        migrate.init_app(app,db)
        
        #marshmallow
        ma.init_app(app)

        #cache
        cache.init_app(app)
