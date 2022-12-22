from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app as app
from flask_praetorian import Praetorian
from flask_marshmallow import Marshmallow
# from udemy.training.models import Users

db=SQLAlchemy()
migrate=Migrate()
guard=Praetorian()
ma=Marshmallow()

def init_extensions(app):

    # sqlalchecmy
    with app.app_context():

        #initialize extensions
        db.init_app(app)
        migrate.init_app(app,db)
        ma.init_app(app)

    # Migrate(app,db)