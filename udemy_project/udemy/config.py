import os


from urllib.parse import quote_plus as urlquote



class BaseConfig(object):
    
    FLASK_DEBUG = False
    TESTING = False

    # developmentconfig=os.getenv('FLASK_ENV')

    APP_DB_USER = os.getenv('APP_DB_USER')
    APP_DB_SECRET = os.getenv("APP_DB_SECRET")
    
    APP_DB_HOST = os.getenv('APP_DB_HOST')
    APP_DB_PORT = os.getenv('APP_DB_PORT')
    
    APP_DB_NAME = os.getenv('APP_DB_NAME')

    SECRET_KEY=os.getenv('SECRET_KEY')

    # SQLALCHEMY_DATABASE_URI = (
    #     f"mssql+pymssql://{APP_DB_USER}:%s@{APP_DB_HOST}:{APP_DB_PORT}/{APP_DB_NAME}"
    #     % quote_plus(APP_DB_SECRET)
    # )
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pymssql://{APP_DB_USER}:%s@{APP_DB_HOST}:{APP_DB_PORT}/{APP_DB_NAME}" % urlquote(str(APP_DB_SECRET))
    )
    # print(SQLALCHEMY_DATABASE_URI)

    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopmentConfig(BaseConfig):
    FLASK_DEBUG = True
    JWT_ACCESS_LIFESPAN = {"minutes": 1}




