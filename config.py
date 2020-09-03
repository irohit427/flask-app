from os import environ

class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///database.sqlite3?check_same_thread+False')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    DB_SERVER = '192.168.1.30'

class DebugConfig(Config):
    DEBUG = True
    SECRET_KEY = environ.get('SECRET_KEY', 'salt_hash')

class ProductionConfig(Config):
    DEBUG = False
    DB_SERVER = '192.168.1.31'
    SECRET_KEY = ('SECRET_KEY')
    VAULT_ADDR = environ.get('VAULT_ADDR')
    VAULT_TOKEN = environ.get('VAULT_TOKEN')
    
class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    SECRET_KEY = 'test_key'
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'
    
app_config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig,
    'Testing': TestingConfig
}