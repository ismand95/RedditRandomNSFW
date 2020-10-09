from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_bootstrap import Bootstrap

cumrade = Flask(__name__)
cumrade.config.from_object(Config)
db = SQLAlchemy(cumrade)
bootstrap = Bootstrap(cumrade)

from cumrade import routes
