from flask import Flask
from flask import render_template
from flask.ext.split import split, finished
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import logging

app = Flask(__name__)
app.secret_key = os.urandom(64)
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
app.config['REDIS_URL'] = redis_url
app.register_blueprint(split)
app.config['SPLIT_DB_FAILOVER'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Debug
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
