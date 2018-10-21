import os

class BaseConfig():

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):

    DEBUG = 'development'


class TestingConfig(DevelopmentConfig):

    TESTING = True
