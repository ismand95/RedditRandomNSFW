from os import urandom


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///subreddits.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = urandom(32)
