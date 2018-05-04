import os

"""Base class"""
class Config(object):
    """Parent configuration Class """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = "0ccd512f8c3493797a23557c32db38e7d51ed74f14fa7580"#os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:deserters@localhost/CrossTownTraffic" #os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True    

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:deserters@localhost/CrossTownTrafficTest" #os.getenv('DATABASE_URL')
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}